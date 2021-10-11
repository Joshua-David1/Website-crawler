import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

valid_links = []

def validate_url(url):
    try:
        return requests.get(url).text
    except Exception:
        return None


def search(base_url):
    global url
    response = validate_url(base_url)
    if response != None:
        html_content = BeautifulSoup(response,'html.parser')
        anchor_tags = html_content.find_all('a')
        for a_tag in anchor_tags:
            link = a_tag.get("href")
            if link is not None:
                link = urljoin(base_url, link)
                if '#' in link:
                    link = link.split('#')[0]
                link = link.strip()
                if link != "None" and len(link) > 0 and url in link:
                    if link not in valid_links:
                        valid_links.append(link)
                        print(f"[+]Link found --> {link}\n")
                        search(link)

url = input("\nWEBSITE TO CRAWL >> ")
print("\n")
search(url)
