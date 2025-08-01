# VWAS - Vulnerable Web App Scanner 🛡️

VWAS is a simple Python tool for detecting potential XSS (Cross-site Scripting) vulnerabilities in web applications.  
It's useful for educational purposes and testing on intentionally vulnerable applications such as `http://testphp.vulnweb.com`.

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/zeljanazegarac/vwas-scanner.git
   cd vwas-scanner

2. Activate a virtual environment (if you're using one):
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the scanner:
   python vwas.py

5. Enter the target URL when prompted, for example:
     Enter URL to scan: http://testphp.vulnweb.com

   
🛠️ Technologies
- Python 3
- requests library
- BeautifulSoup for HTML parsing

⚠️ Disclaimer
Use this tool strictly for educational purposes and only on web applications that explicitly allow vulnerability testing (e.g., testphp.vulnweb.com). Do not use it on unauthorized websites.

📬 Contact
Author: Željana Žegarac
GitHub: zeljanazegarac
