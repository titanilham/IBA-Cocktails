from config import TOKEN, CHAT_ID

import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep



url = "https://iba-world.com/cocktails/all-cocktails/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "Referer": "https://iba-world.com/cocktails/",  
    "Connection": "keep-alive",
}

response = requests.get(url, headers = headers)

html = response.content

soup = BeautifulSoup(html, 'lxml')

block = soup.find("div", class_="cocktail-content").find_all("h2")

for i in block:
    print(i.text.lower())

def main() -> None:
    send_msg("Bot launched")  # start indication
    run = True
    while run:
        if clock() == "12:00:00":
            send_msg("hi")
            sleep(1)
    
def clock() -> str:
    current = datetime.now()
    clock = current.strftime("%H:%M:%S")
    return clock

def send_msg(text: str) -> None:
    url_req = "https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + CHAT_ID + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

if __name__ == "__main__":
    # main()
    pass