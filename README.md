# Security Header Audit PoC (Case: us.gate.com)

*If this research helped you, please consider giving it a ⭐ Star.*


## 🚀 Stay Updated
Found this research useful?
* **Star ⭐** this repo to keep track of it.
* **Follow me** on GitHub for more DeFi security research.
* **Fork** it if you want to run your own experiments.

### ☕ Support the Research
If you appreciate the work and want to support further security research:

<img src="456.PNG" alt="Donate QR" width="200"/>

**Wallet Address (ETH/EVM):** 0xBDDD7973D0DE27B715A4A5cbdb87d0DF78757b3A 


This tool was developed as part of a security audit for **Gate.io US**. It checks for missing HTTP security headers that are critical for protecting financial platforms.

## Vulnerability Overview
During the audit of `us.gate.com`, several key security headers (HSTS, CSP, X-Frame-Options) were found to be missing. 

### Why this matters:
- **Clickjacking:** Without `X-Frame-Options`, the UI can be embedded into malicious sites.
- **M-i-t-M:** Without `Strict-Transport-Security`, users are vulnerable to SSL stripping.
- **XSS:** Without a robust `Content-Security-Policy`, the risk of cross-site scripting increases significantly.

## How to use
```bash
pip install -r requirements.txt
python audit_headers.py us.gate.com
