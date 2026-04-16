# Malicious IP Intelligence System

This project implements a basic threat intelligence system that analyzes IP addresses using the AbuseIPDB API to determine whether they are Safe, Suspicious, or Malicious.

## Overview

The system queries AbuseIPDB to retrieve abuse confidence scores for given IP addresses and classifies them based on predefined thresholds. It also provides basic risk analysis and mitigation strategies.

## Features

- Real-time IP reputation lookup using AbuseIPDB API
- Classification of IPs into:
  - Safe
  - Suspicious
  - Malicious
- Tabular output display
- Basic threat analysis explanation
- Security mitigation recommendations

---

## How It Works

1. Accepts a list of IP addresses
2. Sends request to AbuseIPDB API
3. Retrieves abuse confidence score
4. Classifies IP based on score:
   - > 70 → Malicious
   - 30–70 → Suspicious
   - < 30 → Safe
5. Displays results in structured format

---

## Source Code Structure

- API Integration using `requests`
- Function: `check_ip_reputation(ip)`
- Main execution loop processes multiple IPs
- Error handling for API failures and parsing issues

---

## Sample Output

```
==================================================
Malicious IP Intelligence System
==================================================
IP Address           Status       Score     
--------------------------------------------------
8.8.8.8              Safe         0         
1.1.1.1              Safe         0         
185.220.101.1        Suspicious   45        
45.33.32.156         Malicious    85        
```

---

## Technologies Used

- Python
- Requests Library
- AbuseIPDB API

---

## Security Risks Identified

High-risk IPs may be associated with:
- Brute-force login attempts
- Data exfiltration
- DDoS attacks
- Malware command-and-control servers
- Anonymous networks (e.g., Tor)

---

## Mitigation Strategies

1. Block malicious IPs at firewall level  
2. Integrate API with SIEM tools  
3. Deploy IDS/IPS systems (Snort, Suricata)  
4. Use threat intelligence feeds  
5. Apply egress filtering  
6. Enable logging and alerting  

---

## Important Note

Do NOT expose API keys in source code. Always use environment variables or secure storage mechanisms.

---

## How to Run

```
pip install requests
python3 filename.py
```

---

## Author
Surianandhan Sridhar
