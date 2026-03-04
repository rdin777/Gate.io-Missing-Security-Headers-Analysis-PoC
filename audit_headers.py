import requests
import sys

def audit_headers(url):
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"[*] Analyzing headers for: {url}\n")
    
    # Рекомендуемые заголовки
    security_headers = {
        "Content-Security-Policy": "Prevents XSS and data injection attacks.",
        "Strict-Transport-Security": "Enforces HTTPS connections (prevents SSL Stripping).",
        "X-Frame-Options": "Prevents Clickjacking attacks.",
        "X-Content-Type-Options": "Prevents MIME-sniffing.",
        "Referrer-Policy": "Controls how much referrer information is passed.",
        "Permissions-Policy": "Restricts browser features (camera, microphone, etc.)."
    }

    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        found = 0
        missing = 0

        for header, description in security_headers.items():
            if header in headers:
                print(f"[+] {header}: FOUND")
                found += 1
            else:
                print(f"[-] {header}: MISSING")
                print(f"    Impact: {description}")
                missing += 1
        
        print(f"\n[!] Audit Complete: {found} found, {missing} missing.")
        
    except Exception as e:
        print(f"[!] Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audit_headers(sys.argv[1])
    else:
        # По умолчанию проверяем цель из твоего кейса
        audit_headers("us.gate.com")
