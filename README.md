# Security Header Audit PoC (Case: us.gate.com)

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
