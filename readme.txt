🕵️‍♂️ ROSINT - Recon OSINT Tool

ROSINT is an advanced OSINT (Open Source Intelligence) tool designed to gather valuable public information using powerful search engine dorking and scraping techniques.
⚙️ Environment Setup

Create a virtual environment to keep dependencies isolated:

python3 -m venv venv

Activate the environment:

source venv/bin/activate

📦 Install Required Packages

Install the necessary Python packages:

pip install google-search-results beautifulsoup4 fake-useragent

🚀 How to Run

Use the following command to start ROSINT:

python rosint.py --domain example.com --output json

Replace example.com with your target domain.
Output formats supported: json, txt, etc. (depending on your implementation)
🧠 Pro Tip

Make sure your virtual environment is active before running ROSINT to avoid package issues.
Stay stealthy and scrape responsibly.
