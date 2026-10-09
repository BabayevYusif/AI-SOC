import os
import re
import json
from collections import defaultdict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI SOC Guardian", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class LogAnalysisRequest(BaseModel):
    logs: str

PATTERNS = {
    "SQL Injection": r"(\%27)|(\')|(\-\-)|(\%23)|(#)|(\b(SELECT|UNION|INSERT|DROP|OR\s+1=1|WHERE)\b)",
    "Cross-Site Scripting (XSS)": r"(<script.*?>|%3Cscript.*?%3E|javascript:|alert\(|onerror=)",
    "Directory / Path Traversal": r"(\.\./|\.\.\\|/etc/passwd|windows/win\.ini)",
    "Command Injection": r"(;\s*cat\s+|;\s*ls|\|\s*whoami|/bin/sh|powershell\.exe)"
}

def parse_and_correlate_logs(raw_text: str):
    lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
    findings = []
    ssh_failures = defaultdict(int)

    for line in lines:
        ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
        source_ip = ip_match.group(0) if ip_match else "Unknown"

        matched_category = None
        for category, pattern in PATTERNS.items():
            if re.search(pattern, line, re.IGNORECASE):
                matched_category = category
                break

        if matched_category:
            findings.append({
                "type": matched_category,
                "source_ip": source_ip,
                "raw_log": line
            })

        if "Failed password" in line or "authentication failure" in line or " 401 " in line:
            ssh_failures[source_ip] += 1

    for ip, count in ssh_failures.items():
        if count >= 3:
            findings.append({
                "type": "Brute Force Attack",
                "source_ip": ip,
                "raw_log": f"{count} failed authentication attempts detected from {ip}"
            })

    return {
        "total_lines_inspected": len(lines),
        "suspicious_events_count": len(findings),
        "events": findings[:15]
    }

SOC_SYSTEM_PROMPT = """
You are AI SOC Guardian - a Senior Cybersecurity Incident Responder.
Analyze the security incident summary extracted from server logs.

Return STRICT JSON matching this schema:
{
  "threat_level": "CRITICAL" | "HIGH" | "MEDIUM" | "LOW",
  "threat_score": <integer 0-100>,
  "incident_summary": "<Professional summary of the attack in Azerbaijani>",
  "detected_vectors": [
    {
      "vector": "<e.g. SQL Injection>",
      "attacker_ip": "<IP address>",
      "evidence": "<log snippet>"
    }
  ],
  "remediation_commands": [
    "<Immediate action: iptables rule, netsh rule, or web server config>"
  ],
  "recommendations": [
    "<Security best practice 1>",
    "<Security best practice 2>"
  ]
}
"""

@app.post("/api/analyze")
async def analyze_logs(req: LogAnalysisRequest):
    if not req.logs.strip():
        raise HTTPException(status_code=400, detail="Log məlumatı boşdur.")

    parsed_data = parse_and_correlate_logs(req.logs)

    if parsed_data["suspicious_events_count"] == 0:
        return {
            "threat_level": "LOW",
            "threat_score": 5,
            "incident_summary": "Heç bir anomaliya və ya kiberhücum qeydə alınmadı. Server trafiki təmizdir.",
            "detected_vectors": [],
            "remediation_commands": ["Heç bir bloklama tədbiri tələb olunmur."],
            "recommendations": ["Audit loglarını arxivləyin.", "Standart port təhlükəsizliyini qoruyun."]
        }

    try:
        user_content = f"Events:\n{json.dumps(parsed_data, indent=2)}\n\nRaw Sample:\n{req.logs[:2500]}"
        response = ai_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{SOC_SYSTEM_PROMPT}\n\n{user_content}",
            config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"status": "online", "message": "AI SOC Guardian Engine is Active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
