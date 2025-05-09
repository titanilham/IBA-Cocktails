from config import TOKEN, CHAT_ID

import requests 
from datetime import datetime
from time import sleep

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
    main()