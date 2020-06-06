import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1591400636&sr=8-2'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
PRICE = 160


def getPrice():
    page = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    #cant find id, result is NoneType
    title = soup.find(id="productTitle").get_text()
    print(title)

if __name__ == "__main__":
    getPrice()