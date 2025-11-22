# Self-learning
This repository showcases my hands-on ability to apply security concepts through scripting and tool development. My focus is on creating practical, analyst-ready solutions.

🚀 Practical Projects

1. Log-Hunter (Python Log Analyzer)

A command-line tool written in Python for security log analysis. It automates the detection of common web attack patterns within server access logs.

Functionality: Reads access.log files and uses Regular Expressions (Regex) to flag malicious requests, including:

SQL Injection attempts

Directory Traversal payloads

Known Vulnerability Scanner signatures

* **Project Link:** [Log-Hunter Project Files](./Log_Hunter_Project/README.md)

Output: Generates a structured report detailing suspicious lines and summarizing the Top Attacker IP Addresses by count.

&nbsp;

2. API Threat Intelligence Checker (OSINT Tool)

A Python automation script that integrates with public APIs to perform real-time reconnaissance on suspicious IP addresses, a common task in SOC investigations.

Functionality: Queries the IP-API service to retrieve geolocation and ownership metadata, automatically flagging high-risk indicators:

ISP Verification: Distinguishes between residential/business ISPs and hosting providers.

VPN/Proxy Detection: Alerts if the IP belongs to a data center (often used to mask attacker location).

JSON Parsing: Extracts and formats raw API data into readable intelligence.

* **Project Link:** [Threat Intel Project Files](./Threat_Intel_Project/README.md)

Output: Produces a "Threat Intelligence Report" classifying the IP target as High Risk (Hosting/VPN) or Lower Risk (Residential).
