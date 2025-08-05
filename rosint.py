# This tool is designed to perform Google/Bing Dorking,
# with modular design, clean code, and export capabilities.

# STEP 1: Import required libraries
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import argparse
import json
import time
import os

# STEP 2: Define dork templates (can be expanded or loaded from file)
def generate_dorks(domain):
    dorks = [
        f"site:{domain} intitle:'index of'",
        f"site:{domain} inurl:login",
        f"site:{domain} ext:sql | ext:log | ext:bak",
        f"site:{domain} intext:'password'",
        f"site:{domain} filetype:pdf",
        f"site:{domain} 'admin login'"
    ]
    return dorks

# STEP 3: Perform search using Bing (Google blocks scrapers)
def search_bing(query):
    try:
        headers = {'User-Agent': UserAgent().random}
        url = f"https://www.bing.com/search?q={query}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('http') and 'bing.com' not in href:
                links.append(href)

        return links

    except Exception as e:
        print(f"[!] Error searching Bing: {e}")
        return []

# STEP 4: Run the OSINT process and collect data
def run_osint(domain, output_format):
    dorks = generate_dorks(domain)
    all_results = {}

    print(f"[+] Starting OSINT scan on: {domain}\n")

    for dork in dorks:
        print(f"[*] Dork: {dork}")
        results = search_bing(dork)
        all_results[dork] = results

        for link in results:
            print(f"    [-] {link}")

        time.sleep(2)  # pause between queries

    save_results(domain, all_results, output_format)

# STEP 5: Save results to file (JSON or TXT)
def save_results(domain, results, output_format='json'):
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    filename = f"results_{domain}_{timestamp}.{output_format}"

    if not os.path.exists("results"):
        os.mkdir("results")

    filepath = os.path.join("results", filename)

    try:
        if output_format == 'json':
            with open(filepath, 'w') as f:
                json.dump(results, f, indent=4)

        elif output_format == 'txt':
            with open(filepath, 'w') as f:
                for dork, links in results.items():
                    f.write(f"DORK: {dork}\n")
                    for link in links:
                        f.write(f"    {link}\n")
                    f.write("\n")

        print(f"\n[+] Results saved to: {filepath}")

    except Exception as e:
        print(f"[!] Error saving file: {e}")

# STEP 6: CLI interface to make the tool user-friendly
def main():
    parser = argparse.ArgumentParser(description='Advanced OSINT Dorking Tool')
    parser.add_argument('--domain', required=True, help='Target domain (e.g., example.com)')
    parser.add_argument('--output', choices=['json', 'txt'], default='json', help='Output format')

    args = parser.parse_args()

    run_osint(args.domain, args.output)

# STEP 7: Run main if this file is executed directly
if __name__ == '__main__':
    main()
