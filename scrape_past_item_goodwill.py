import requests
from bs4 import BeautifulSoup

def get_ended_item_url(item):
    response = requests.get("https://shopgoodwill.com/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", text=lambda x: x and item.lower() in x.lower())
        for link in links:
            parent = link.parent
            if parent and "Ended On: " in parent.get_text():
                return link["href"]
    return None

item = "Raf Simons"
url = get_ended_item_url(item)

if url:
    print(f"Found {item} at {url}")
else:
    print(f"Could not find {item}")
