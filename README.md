# Self-learning
This repository showcases my hands-on ability to apply security concepts through scripting and tool development. My focus is on creating practical, analyst-ready solutions.

🚀 Practical Projects

1. Log-Hunter (Python Log Analyzer)

A command-line tool written in Python for security log analysis. It automates the detection of common web attack patterns within server access logs.

Functionality: Reads access.log files and uses Regular Expressions (Regex) to flag malicious requests, including:

SQL Injection attempts

Directory Traversal payloads

Known Vulnerability Scanner signatures

* **Project:** Log_Hunter_Project

Output: Generates a structured report detailing suspicious lines and summarizing the Top Attacker IP Addresses by count.

&nbsp;

2. API Threat Intelligence Checker (OSINT Tool)

A Python automation script that integrates with public APIs to perform real-time reconnaissance on suspicious IP addresses, a common task in SOC investigations.

Functionality: Queries the IP-API service to retrieve geolocation and ownership metadata, automatically flagging high-risk indicators:

ISP Verification: Distinguishes between residential/business ISPs and hosting providers.

VPN/Proxy Detection: Alerts if the IP belongs to a data center (often used to mask attacker location).

JSON Parsing: Extracts and formats raw API data into readable intelligence.

* **Project Link:** [self learning Project Files](./Threat_Intel_Project/README.md)

Output: Produces a "Threat Intelligence Report" classifying the IP target as High Risk (Hosting/VPN) or Lower Risk (Residential).

&nbsp;

3. Splunk SOC Setup (Log Ingestion and Administration)

A foundational hands-on project demonstrating the deployment and configuration required to establish a working Security Information and Event Management (SIEM) environment using Splunk Enterprise.

Functionality: Installed and configured the Splunk Indexer on an Ubuntu Linux virtual machine.

Deployed and configured Universal Forwarders on separate Windows and Linux test systems.

Established secure log collection pipelines to ingest critical data sources, including Windows Event Logs and standard Syslogs.

Used basic Search Processing Language (SPL) commands to validate successful log flow and index creation.

* **Project Link:** [self learning Project Files](./Splunk_SOC_Setup_Main/README.md)
