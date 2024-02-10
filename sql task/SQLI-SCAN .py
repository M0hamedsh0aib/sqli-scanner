import requests
from urllib.parse import urlparse, parse_qs
import argparse
import banner   

def get_params(url):
    params = parse_qs(urlparse(url).query)
    if params:
        return {i: '\ ' ' --' for i, j in params.items()}
    else:
        return None
    
def scan(url, params):
    r = requests.get(url, params=params)
    if ('error' in r.text.lower()) or ('sql' in r.text.lower()):
        print(f"Vulnerability Detected in {url}")
    else:
        print(f"No Vulnerability Detected in {url}")

def main():
    url = banner.banner() 
    params = get_params(url)
    if params:
        scan(url, params)
    else:
        print(f"No parameters found in {url}")

if __name__ == "__main__":
    main()
