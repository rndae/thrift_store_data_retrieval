import requests
from bs4 import BeautifulSoup

def get_items_by_date(date):
    items = []
    response = requests.get("https://shopgoodwill.com/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=lambda x: x and date in x)
        for link in links:
            text = link.get_text().strip()
            url = link["href"]
            parent = link.parent
            if parent and "Ends On: " in parent.get_text():
                items.append((text, url))
    return items

date = "6/20/2023"
items = get_items_by_date(date)


for item in items:
    print(item[0], "-", item[1])
