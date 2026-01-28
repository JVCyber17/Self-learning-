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

* **Project:** Threat_Intel_Project

Output: Produces a "Threat Intelligence Report" classifying the IP target as High Risk (Hosting/VPN) or Lower Risk (Residential).

&nbsp;

3. Splunk SOC Setup (Log Ingestion and Administration)

A foundational hands-on project demonstrating the deployment and configuration required to establish a working Security Information and Event Management (SIEM) environment using Splunk Enterprise.

Functionality: Installed and configured the Splunk Indexer on an Ubuntu Linux virtual machine.

Deployed and configured Universal Forwarders on separate Windows and Linux test systems.

Established secure log collection pipelines to ingest critical data sources, including Windows Event Logs and standard Syslogs.

Used basic Search Processing Language (SPL) commands to validate successful log flow and index creation.

* **Project:** Splunk_SOC_Setup_Main

&nbsp;

4. Cyber Shield (Prompt Engineering & AI Advisory)

A project demonstrating rapid prototyping and the capability to transform a generic Large Language Model (LLM) into a highly specialized, structured advisory tool for complex cybersecurity domains.

Functionality: 
Persona Engineering: Programmed a custom Senior Consultant persona with a Master's-level authority using pure text instructions.

Structured Advice: Enforces a rigid "Define, Risk, Mitigate" methodology for all responses, ensuring analytical depth instead of general information.

Domain Specialization: Limits the focus to advanced areas including Network Defense, Cloud Security (AWS/Azure), and Incident Response (IR).

Tool Deployment: Successfully deployed the custom-programmed bot on a public platform (Poe/GPTs) for external access and demonstration.

* **Project:** Cyber_Shield_Project

Output: A functional, specialized AI consultant that provides professional, structured analysis and strategic recommendations on complex cybersecurity challenges.

&nbsp;

5. Information Gathering Tool (Python Reconnaissance)

A command line utility written in Python for ethical network reconnaissance and IP information collection. It automates the process of gathering preliminary intelligence on network targets for security assessments.

Functionality:
Validates command line input and performs automated network checks on a target IP address, including

Connectivity checks to determine if the target is online 

Reverse DNS Search to identify the hostname of the target 

Port Discovery for common services like SSH and Web 

Organization Lookup for geolocation and ownership data via API 

* **Project:** Metbrains_P1.Main

Output Results are displayed directly in the console and automatically appended to a structured scanlog text file for documentation.

&nbsp;

6. Automated NSE Reconnaissance

This is a custom tool we built using the Nmap Scripting Engine to make the discovery phase much faster. It is a smart scanner that adapts its behavior based on the ports it finds so you don't have to run multiple manual commands.

What it does:
The tool is written in Lua and runs directly within the Nmap scan process for maximum efficiency. It uses specialized libraries to identify web services and extract page titles automatically. Actually, it also probes for hidden files like robots.txt to find sensitive directories that might be left exposed. Still, it doesn't just focus on the web. It pulls version data for every open port to help flag outdated or vulnerable servers that need patching.

* **Project:** NSE script for collecting host and network based information.

Output It produces a structured report inside your Nmap scan results that lists the target IP, service versions, and any web intelligence it gathered during the run.
