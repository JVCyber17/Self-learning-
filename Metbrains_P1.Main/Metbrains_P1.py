import sys
import socket
import subprocess
import platform
import json
import urllib.request

def run_investigation():
    # We check if you actually typed an IP after the script name
    if len(sys.argv) < 2:
        print("You forgot to give me an IP address")
        print("Try something like python Metbrains_P1.py 8.8.8.8")
        return

    target = sys.argv[1]
    results = []
    results.append(f"Report for {target}")
    
    # 1. The Connectivity Check
    system_type = platform.system().lower()
    flag = "n" if system_type == "windows" else "c"
    try:
        subprocess.check_output(["ping", f"-{flag}", "1", target], stderr=subprocess.STDOUT)
        status = "The target is online"
    except Exception:
        status = "The target did not respond to ping"
    results.append(status)

    # 2. Reverse DNS Search
    try:
        name_info = socket.gethostbyaddr(target)
        hostname = f"Hostname found. {name_info[0]}"
    except Exception:
        hostname = "No hostname could be found"
    results.append(hostname)

    # 3. Port Discovery
    found_ports = []
    # Checking common ones like SSH and Web
    for port in [22, 80, 443]:
        test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_sock.settimeout(0.5)
        if test_sock.connect_ex((target, port)) == 0:
            found_ports.append(str(port))
        test_sock.close()
    
    if found_ports:
        port_msg = f"Open ports discovered. {', '.join(found_ports)}"
    else:
        port_msg = "No common ports are open"
    results.append(port_msg)

    # 4. Organization Lookup
    try:
        api_url = f"http://ip-api.com/json/{target}"
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())
            org = data.get("org", "Unknown Owner")
            location = f"{data.get('city')}, {data.get('country')}"
            whois = f"Owned by {org} located in {location}"
    except Exception:
        whois = "Could not find organization data"
    results.append(whois)

    # Output to terminal
    print("\n" + "\n".join(results) + "\n")

    # Saving to the text file automatically
    with open("scanlog.txt", "a") as f:
        f.write("=" * 20 + "\n")
        f.write("\n".join(results) + "\n")
    
    print("Results have been saved to scanlog.txt")

if __name__ == "__main__":
    run_investigation()
