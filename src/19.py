import requests
from bs4 import BeautifulSoup
import os

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    
    for link in soup.find_all("a"):
        href = link.get("href")
        print(href)

if __name__ == "__main__":
    url = "https://www.example.com"
    html = fetch_html(url)
    if html:
        parse_html(html)
