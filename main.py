from bs4 import BeautifulSoup
import requests

# for now we are working with newegg graphics cards but we can change the catalog we are looking for later.
url = "https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

items = doc.find_all("div", class_="item-container")
numCards = 0
for item in items:
    numCards = numCards + 1
    name = item.find("a", class_="item-title").text.strip()
    price = item.find("li", class_="price-current").find("strong").text.strip()
    print("Name:", name)
    print("Price: $" + price)
    print()
print("Number of cards available: "+ str(numCards))
