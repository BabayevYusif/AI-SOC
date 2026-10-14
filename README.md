# 🛡️ AI SOC Guardian
### AI-Powered Cybersecurity Platform

**A lightweight, AI-powered Security Operations Center (SOC) assistant designed for small businesses, startups, and independent developers.**

---

## 📌 Problem & Mission

Small businesses, startups, and independent developers often lack access to dedicated 24/7 Security Operations Center (SOC) teams or enterprise-grade Security Information and Event Management (SIEM) platforms such as Splunk and Datadog.

These solutions can be expensive, technically complex, and difficult to maintain for organizations with limited resources.

As a result, many organizations experience **log blindness** — a situation in which critical cybersecurity threats remain hidden within thousands of raw server log entries.

**AI SOC Guardian** aims to solve this challenge by providing an accessible, intelligent, and automated cybersecurity monitoring solution.

Our platform is designed to:

- Analyze large volumes of server logs efficiently.
- Identify suspicious activities and potential cyberattacks.
- Correlate security events using artificial intelligence.
- Evaluate potential threats and assign risk scores.
- Generate actionable incident reports and remediation recommendations.
- Help developers and small organizations improve their security posture.

---

## ⚡ Why Gemini AI Beyond Standard Regex?

Traditional rule-based detection systems rely heavily on predefined patterns and regular expressions (regex). Although effective for identifying known threats, these approaches can struggle with complex attack sequences and unfamiliar payloads.

**AI SOC Guardian integrates Gemini 2.5 Flash** to provide contextual security analysis beyond conventional pattern matching.

### 1. Multi-Stage Attack Chain Correlation

- Connects suspicious events occurring across different log entries.
- Identifies relationships between reconnaissance, brute-force attempts, and injection attacks.
- Produces a unified incident narrative to help analysts understand potential attack sequences.

### 2. Contextual & Obfuscated Payload Analysis

- Analyzes suspicious and potentially obfuscated payloads.
- Identifies attack patterns that may evade basic signature-based detection.
- Provides contextual explanations of suspicious requests and possible attacker intentions.
- Assists in investigating unfamiliar attack variations.

### 3. AI-Assisted Incident Remediation

- Generates recommended defensive actions based on identified threats.
- Suggests firewall rules using `iptables` or `netsh`.
- Provides Nginx security-hardening recommendations.
- Recommends secure configuration changes and potential code fixes.
- Produces remediation scripts for administrator review before deployment.

---

## 🏗️ System Architecture

AI SOC Guardian combines local log processing, artificial intelligence, and an interactive security dashboard into a unified workflow.

### 1. Raw Server Log Collection

**Supported inputs:**
- `.log` files
- `.txt` files
- Manually pasted server logs

### 2. Local Heuristic Parser — Python

**Technology:** Python (`main.py`), regex, and event counters.

**Responsibilities:**
- Processes large volumes of raw server logs.
- Detects suspicious patterns and repeated authentication failures.
- Identifies potential brute-force activity.
- Aggregates security events associated with suspicious IP addresses.
- Filters relevant events to reduce unnecessary AI processing and token consumption.

### 3. Gemini AI SOC Engine

**Technology:** Google Gemini 2.5 Flash

**Responsibilities:**
- Analyzes suspicious security events identified by the local parser.
- Correlates attack patterns with HTTP response codes and event sequences.
- Evaluates potential attack intent and severity.
- Assigns a risk score ranging from **0 to 100**.
- Generates structured JSON incident reports.
- Provides contextual explanations and recommended remediation actions.

### 4. SOC Frontend Dashboard

**Technologies:** Next.js and Tailwind CSS

**Features:**
- Interactive cybersecurity monitoring dashboard.
- Visual threat severity indicators.
- Security incident timelines.
- Suspicious IP address analysis.
- Detailed attack payload inspection.
- MITRE ATT&CK and OWASP threat mappings.
- JSON incident report exports.
- Downloadable defensive shell scripts.

---

## 🔄 Security Analysis Workflow

**Step 1 — Log Ingestion**

Users upload or paste server logs into the platform.

**Step 2 — Local Threat Detection**

The Python-based heuristic engine scans the logs and extracts potentially malicious activities.

**Step 3 — AI-Powered Analysis**

Gemini 2.5 Flash analyzes the selected events, identifies possible attack patterns, and evaluates their severity.

**Step 4 — Incident Reporting**

The platform generates a structured security report containing detected threats, risk scores, suspicious IP addresses, and recommended actions.

**Step 5 — Security Visualization**

The frontend dashboard presents the analysis results through interactive security indicators and incident details.

**Step 6 — Remediation Recommendations**

Users can review and export recommended defensive configurations and scripts to help mitigate identified threats.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Backend | Python |
| Local Threat Detection | Regex & Heuristic Analysis |
| AI Engine | Google Gemini 2.5 Flash |
| Frontend | Next.js |
| Styling | Tailwind CSS |
| Incident Reports | JSON |
| Security Frameworks | MITRE ATT&CK & OWASP |
| Remediation | iptables, netsh & Nginx |

---

## 🎯 Target Users

AI SOC Guardian is designed for:

- **Small and Medium-Sized Businesses (SMBs)** — Organizations without dedicated cybersecurity teams.
- **Startups** — Growing companies seeking accessible security monitoring.
- **Independent Developers** — Developers managing their own applications and servers.
- **Small IT Teams** — Teams requiring faster log analysis and incident investigation.
- **Cybersecurity Students** — Learners exploring threat detection, log analysis, and AI-assisted security operations.

---

## 🚀 Project Vision

Our vision is to make intelligent cybersecurity monitoring more accessible, affordable, and practical.

By combining traditional detection techniques with modern artificial intelligence, **AI SOC Guardian** aims to reduce the complexity of security analysis and help smaller organizations identify and respond to potential threats more effectively.

**Our mission is simple: Make AI-powered cybersecurity accessible to everyone.**

---

## 👥 Team Members

- **Yusif Babayev** — **Product / Project Lead**  
  GitHub: [@BabayevYusif](https://github.com/BabayevYusif)

- **Nijat Safarov** — **Data / ML & Backend Developer**  
  GitHub: [@nicat700-ctrl](https://github.com/nicat700-ctrl)

- **Rasul Mammadli** — **Developer / Engineer**  
  GitHub: [@RasulMammadli](https://github.com/RasulMammadli)

---

### 🛡️ AI SOC Guardian — Smarter Detection. Faster Analysis. Stronger Security..
