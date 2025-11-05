import re
from collections import Counter

# Our list of "bad guy" patterns to look for
patterns = {
    "SQL_INJECTION": r"(\'|\%27)\s*(OR|UNION)\s*(\'|\%27|SELECT|--)",
    "DIRECTORY_TRAVERSAL": r"(\.\.\/|\.\.\\)",
    "FILE_INCLUSION": r"(etc\/passwd|boot\.ini)",
    "NMAP_SCANNER": r"Nmap Scripting Engine"
}

def analyze_log(log_file):
    print(f"Analyzing {log_file}...")
    
    suspicious_lines = []
    attacker_ips = []

    try:
        with open(log_file, 'r') as f:
            
            # Read the file line by line
            for line_number, line in enumerate(f, 1):
                found_attack = None
                
                # Try to find the IP address at the start of the line
                ip_match = re.search(r"^([\d\.]+)", line)
                if ip_match:
                    ip = ip_match.group(1)
                else:
                    ip = "UNKNOWN_IP"

                # Now, check that line against all our "bad" patterns
                for attack_type, pattern in patterns.items():
                    if re.search(pattern, line, re.IGNORECASE):
                        found_attack = attack_type
                        break # Found one, stop checking this line
                
                # If we found an attack, save the IP and the line
                if found_attack:
                    suspicious_lines.append(f"Line {line_number}: {found_attack} from IP {ip}")
                    attacker_ips.append(ip)

    except FileNotFoundError:
        print(f"Error: Could not find the file {log_file}")
        return

    # --- Print the Report ---
    print("\n--- ANALYSIS COMPLETE ---")
    
    if not suspicious_lines:
        print("No suspicious activity found.")
        return

    print(f"\nTotal Suspicious Lines: {len(suspicious_lines)}")
    
    # Count the IPs
    print("\nTop Attacker IPs:")
    ip_counts = Counter(attacker_ips)
    for ip, count in ip_counts.most_common(3):
        print(f"    {ip}: {count} attempts")

    print("\nAttack Details:")
    for suspicious_line in suspicious_lines:
        print(f"    {suspicious_line}")
        
    print("\n--- END OF REPORT ---")


# This is where the script starts
analyze_log("sample_access.log")
