import requests

# AbuseIPDB API Key
API_KEY = ""

# List of IP addresses to analyze
ips = [
    "8.8.8.8",
    "1.1.1.1",
    "185.220.101.1",
    "45.33.32.156"
]

def check_ip_reputation(ip):
    """Check IP reputation using AbuseIPDB API"""
    url = "https://api.abuseipdb.com/api/v2/check"
    
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        score = data["data"]["abuseConfidenceScore"]
        
        if score > 70:
            status = "Malicious"
        elif score > 30:
            status = "Suspicious"
        else:
            status = "Safe"
        
        return status, score
    except requests.exceptions.RequestException as e:
        return "Error", f"API request failed: {e}"
    except (KeyError, ValueError) as e:
        return "Error", f"Failed to parse response: {e}"

def main():
    print("=" * 50)
    print("Malicious IP Intelligence System")
    print("=" * 50)
    print(f"{'IP Address':<20} {'Status':<12} {'Score':<10}")
    print("-" * 50)
    
    for ip in ips:
        status, score = check_ip_reputation(ip)
        if status == "Error":
            print(f"{ip:<20} {status:<12} {score:<10}")
        else:
            print(f"{ip:<20} {status:<12} {score:<10}")
    
    print("\nRisk Analysis:")
    print("-" * 50)
    print("High-confidence malicious IPs pose threats including:")
    print("  • Unauthorized access via brute-force attacks")
    print("  • Data breaches through data exfiltration")
    print("  • DDoS attacks overwhelming services")
    print("  • Malware distribution from C2 servers")
    print("  • Anonymized attacks via Tor exit nodes")
    
    print("\nMitigation Recommendations:")
    print("-" * 50)
    print("1. Block malicious IP addresses at firewall level")
    print("2. Integrate AbuseIPDB into SIEM pipelines for automated blocking")
    print("3. Deploy IDS such as Snort or Suricata")
    print("4. Subscribe to updated threat intelligence feeds")
    print("5. Implement egress filtering rules")
    print("6. Log and alert on suspicious IP traffic")

if __name__ == "__main__":
    main()
