import requests  # The tool that lets Python 'browse' the web
import json      # The tool that helps Python read the data format
import sys       # Used to get command line arguments

def get_ip_intelligence(ip_address):
    print(f"[-] Querying global database for: {ip_address}...")

    # 1. Define the API URL
    # We are using ip-api.com, a free public database.
    api_url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,city,isp,org,hosting,query"

    try:
        # 2. Make the Request (Send the "letter")
        response = requests.get(api_url, timeout=10)
        
        # 3. Check if the API worked (Status Code 200 means "OK")
        if response.status_code != 200:
            print(f"[!] Error: API returned status code {response.status_code}")
            return

        # 4. Read the Data (Parse the JSON)
        data = response.json()

        # 5. Analyze the Result
        if data['status'] == 'fail':
            print(f"[!] API Error: {data['message']}")
            return

        # --- GENERATE REPORT ---
        print("\n" + "="*40)
        print(f"   THREAT INTELLIGENCE REPORT: {ip_address}")
        print("="*40)
        
        print(f"[*] Location:      {data['city']}, {data['country']}")
        print(f"[*] ISP:           {data['isp']}")
        print(f"[*] Organization:  {data['org']}")
        
        # This is a key security check: Is this a hosting provider?
        is_hosting = data.get('hosting', False)
        if is_hosting:
             print(f"[*] Type:          ⚠️  DATA CENTER / VPN DETECTED (High Risk)")
        else:
             print(f"[*] Type:          Residential/Business (Lower Risk)")
             
        print("="*40 + "\n")

    # SPECIFIC ERROR HANDLING FOR NO INTERNET
    except requests.exceptions.ConnectionError:
        print("\n[!] CRITICAL ERROR: Could not connect to the internet.")
        print("    Please ensure your WiFi is on and you are not blocked by a firewall.")
        print("    (Note: This script will NOT work in most online code editors like browser-based IDEs)")
    except requests.exceptions.Timeout:
        print("\n[!] ERROR: The request timed out. The server took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"\n[!] Network Error: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    # Default target
    target_ip = "8.8.8.8" 
    
    # Check if user provided an IP in the terminal
    if len(sys.argv) > 1:
        # Take the first argument (ignoring the script name)
        # Example: python threat_check.py 1.1.1.1 -> target_ip becomes "1.1.1.1"
        target_ip = sys.argv[1]
        # Clean up any accidental flags like --input if they sneak in
        if target_ip.startswith("--"):
            target_ip = "8.8.8.8"
            print("[!] Warning: Invalid argument detected. Defaulting to 8.8.8.8")

    get_ip_intelligence(target_ip)
