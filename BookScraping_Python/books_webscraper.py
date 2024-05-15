import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1
proceed = True

data =[]
while (proceed):

    url = "https://books.toscrape.com/catalogue/page-" +str(current_page)+".html"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    if soup.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for book in all_books:
        item = {}
        item["title"] = book.find("img").attrs["alt"]
        item["link"] = "https://books.toscrape.com/catalogue/" + book.find("a").attrs["href"]
        item["price"] = book.find("p", class_="price_color").text[2:]
        item["stock availability"] = book.find("p", class_="instock availability").text.strip()
        data.append(item)
    print("Scraped page-" + str(current_page))
    current_page += 1

df = pd.DataFrame(data)
df.to_excel("books.xlsx")
