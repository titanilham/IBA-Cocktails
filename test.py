import requests 
from datetime import datetime
from time import sleep

def main():
    run = True
    while run:
        if clock() == "12:00:00":
            send_msg("hi")
            sleep(1)
    
def clock():
    current = datetime.now()
    clock = current.strftime("%H:%M:%S")
    return clock

def send_msg(text: str) -> None:
    token = "6304566943:AAFZPJrYnIkyyl3xXiEvO822Hs3urZsq6zQ"
    chat_id = "1456945518"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


if __name__ == "__main__":
    main()