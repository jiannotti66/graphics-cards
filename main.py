from bs4 import BeautifulSoup
import requests

def findCards(maxPrice, url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    items = doc.find_all("div", class_="item-container")
    numCards = 0
    for item in items:
        numCards = numCards + 1
        name = item.find("a", class_="item-title").text.strip()
        price_str = item.find("li", class_="price-current").find("strong").text.strip()
        if price_str == "COMING SOON":
            # Skip items labeled as "COMING SOON"
            continue
        price = int(price_str.replace(',', ''))
        if price < maxPrice:
            print("Name:", name)
            print("Price: $" + price_str)
            print()
            
    print("Number of cards available: " + str(numCards))

findCards(500, "https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48")
