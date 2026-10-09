# 🛡️ AI SOC Guardian — AI-Powered Cybersecurity Platform

> **A pocket-sized, autonomous AI SOC analyst built for SMBs, startups, and solo developers.**

---

## 📌 Problem & Mission
Solo developers, small IT teams, and start-ups who host web servers frequently lack the luxury of dedicated 24/7 Security Operations Center (SOC) personnel or enterprise SIEM platforms (Splunk, Datadog, etc.) due to prohibitive pricing and complex setups.

As a result, they suffer from **log blindness**: raw server logs contain critical breach signals, but manually analyzing hundreds of thousands of lines during or after an incident is slow, complex, and prone to human error. **AI SOC Guardian** bridges this gap by ingesting raw web server activity, triaging intrusions in real time, and generating actionable remediation scripts instantly.

---

## ⚡ Why Gemini AI Beyond Standard Regex?
While traditional regex rules excel at surface-level pattern matching, the **Gemini 2.5 Flash** triage engine performs 3 critical cybersecurity tasks:
1. **Multi-Stage Attack Chain Correlation:** Connects disparate events (e.g., reconnaissance scanning followed by an SSH brute force and subsequent SQL injection) into a unified, coherent incident narrative.
2. **Contextual & Obfuscated Payload Understanding:** Decodes complex, obfuscated, and zero-day payload variations that evade static signatures.
3. **Automated Incident Remediation:** Automatically produces production-ready server defense configurations, such as immediate `iptables`/`netsh` firewall block commands, Nginx hardening directives, and secure code patches.

---

## 🏗️ System Architecture

```text
[ Raw Server Logs (.log, .txt, text paste) ]
                     │
                     ▼
  1. LOCAL HEURISTIC PARSER (main.py regex & counters)
     ├── Rapidly filters thousands of lines for high-entropy indicators
     ├── Aggregates repeated authentication failures (Brute Force)
     └── Isolates suspicious threat actors to minimize LLM token overhead
                     │
                     ▼
  2. GEMINI AI SOC ENGINE (gemini-2.5-flash)
     ├── Correlates security anomalies with HTTP status codes
     ├── Determines root cause, attack intent, and severity score (0–100)
     └── Outputs structured JSON with immediate remediation actions
                     │
                     ▼
  3. SOC FRONTEND DASHBOARD (Next.js & Tailwind CSS)
     ├── Visualizes live threat gauge, timeline, and attacker IP distributions
     ├── Displays attack payloads alongside MITRE ATT&CK / OWASP mappings
     └── One-click export for JSON incident reports and defensive shell scripts
