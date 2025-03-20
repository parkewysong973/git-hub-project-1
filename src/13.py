import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for article in soup.find_all("div", class_="article"):
        title = article.h3.a.text
        link = article.h3.a["href"]
        description = article.p.text.strip()
        authors = [author.text for author in article.find("strong").text.split(", ")]
        articles.append({"title": title, "link": link, "description": description, "authors": authors})
    return articles

articles = fetch_articles("https://example.com/articles/")
for article in articles:
    print(f"Title: {article['title']}")
    print(f"Link: {article['link']}")
    print(f"Description: {article['description']}")
    print(f"Authors: {', '.join(article['authors'])}\n")
