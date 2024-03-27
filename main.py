from bs4 import BeautifulSoup;
import requests;

url = "https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify)

prices = doc.find_all(text="$")
print(prices)
