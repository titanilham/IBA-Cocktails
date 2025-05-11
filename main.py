from config import TOKEN, CHAT_ID

import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import random

def parser():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "Referer": "https://iba-world.com/cocktails/",  
        "Connection": "keep-alive",
    }

    iba_cocktails = [
    "alexander", "americano", "angel-face", "aviation", "bees-knees", "bellini",
    "between-the-sheets", "black-russian", "bloody-mary", "boulevardier", "bramble",
    "brandy-alexander", "brandy-crusta", "caipirinha", "canchanchara", "cardinale",
    "casino", "champagne-cocktail", "clover-club", "corpse-reviver-2", "cosmopolitan",
    "cuba-libre", "daiquiri", "dark-n-stormy", "dry-martini", "espresso-martini",
    "french-75", "french-connection", "garibaldi", "gin-basil-smash", "gin-fizz",
    "golden-dream", "grasshopper", "hanky-panky", "harvey-wallbanger", "hemingway-special",
    "horses-neck", "illegal", "irish-coffee", "john-collins", "jungle-bird",
    "kir", "last-word", "lemon-drop-martini", "long-island-iced-tea", "mai-tai",
    "manhattan", "margarita", "martinez", "mary-pickford", "mimosa", "mint-julep",
    "missionarys-downfall", "mojito", "moscow-mule", "naked-and-famous", "negroni",
    "new-york-sour", "old-cuban", "old-fashioned", "paloma", "paper-plane",
    "paradise", "penicillin", "pina-colada", "pisco-punch", "pisco-sour",
    "planters-punch", "porn-star-martini", "porto-flip", "rabo-de-galo", "ramos-gin-fizz",
    "remember-the-maine", "rusty-nail", "sazerac", "sea-breeze", "sex-on-the-beach",
    "sherry-cobbler", "sidecar", "singapore-sling", "south-side", "spicy-fifty",
    "spritz", "stinger", "suffering-bastard", "tequila-sunrise", "three-dots-and-a-dash",
    "tommys-margarita", "trinidad-sour", "tuxedo", "vesper", "vieux-carre",
    "whiskey-sour", "white-lady", "zombie"
]

    for i in iba_cocktails:
        
        random_cocktail = random.choice(iba_cocktails)
        try:
            url_cocktail = f"https://iba-world.com/iba-cocktail/{random_cocktail}/"
            response_cocktails = requests.get(url_cocktail, headers = headers)
            html_cocktails = response_cocktails.content
            soup_cocktails = BeautifulSoup(html_cocktails, 'lxml')
            
            ingredients = soup_cocktails.find_all("div", class_="elementor-shortcode")
            
            for j in ingredients:
                ul_tags = j.find_all("ul")
                for ul in ul_tags:
                    return f"{random_cocktail.title()}\nIngredients:\n{ul.text}"
        except: 
            print(f"Error\nCocktail {random_cocktail} - is not found")
            send_msg(f"Error")
            main()
            
    
def main() -> None:
    send_msg("Bot launched")  # start indication
    run = True
    while run:
        if clock() == "12:00:00":
            send_msg(parser())
            
    
def clock() -> str:
    current = datetime.now()
    clock = current.strftime("%H:%M:%S")
    return clock

def send_msg(text: str) -> None:
    try:
        url_req = "https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + CHAT_ID + "&text=" + text
        results = requests.get(url_req)
    except:
        
        print("404 Not Found")
        sleep(5)
        url_req = "https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + CHAT_ID + "&text=" + "404 Not Found"
        main()
    print(results.json())

if __name__ == "__main__":
    main()
