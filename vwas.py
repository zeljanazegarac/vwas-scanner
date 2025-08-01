from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

XSS_PAYLOAD = "<script>alert(1)</script>"

def get_forms(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[!] Error fetching forms: {e}")
        return []

def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        name = input_tag.attrs.get("name")
        if name:
            inputs.append({"type": input_type, "name": name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, payload):
    action = form_details["action"]
    if not action.startswith("/"):
        action = "/" + action
    target_url = urljoin(url, action)

    data = {}
    for input in form_details["inputs"]:
        if input["type"] == "text":
            data[input["name"]] = payload
        else:
            data[input["name"]] = "test"

    print(f"[*] Submitting form to {target_url} with payload...")
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    forms = get_forms(url)
    print(f"[*] Detected {len(forms)} form(s) on {url}")
    
    for i, form in enumerate(forms):
        form_details = get_form_details(form)
        response = submit_form(form_details, url, XSS_PAYLOAD)

        if XSS_PAYLOAD in response.text:
            print(f"[!!!] Potential XSS vulnerability in form #{i+1} at {form_details['action']}")
        else:
            print(f"[+] Form #{i+1} seems safe")

if __name__ == "__main__":
    target = input("Enter URL to scan: ")
    scan_xss(target)

