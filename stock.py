import requests
from bs4 import BeautifulSoup

def get_stock():
    stock = "2330"

    url = f"https://tw.stock.yahoo.com/quote/{stock}"

    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    price_tag = soup.find("span", {"class": "Fz(32px)"})

    if not price_tag:
        return stock, "抓不到價格"

    return stock, price_tag.text


def send_telegram(msg):
    token = "7583187667:AAGanE6j93RoZBpIY_Ho8-ZAEEZOfS4V0gA"
    chat_id = "8780609556"

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(url, data={
        "chat_id": chat_id,
        "text": msg
    })


stock, price = get_stock()
message = f"📈 股票 {stock} 現價：{price}"

send_telegram(message)

stock, price = get_stock()
print("結果：", stock, price)