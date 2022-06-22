import requests
from .force_types import force_type
from threading import Thread
from time import sleep

fetching = False

def loading():
    """loading animation for exists fetch function"""
    i = 0
    Misc.cursor(0)
    while fetching:
        i = (i + 1) % 3
        print(f"fetching data{'.' * i}\r", end="", flush=True)
        sleep(0.05)
    Misc.cursor(1)

def exists(user: str) -> bool:
    global fetching
    """returns if user exists on replit"""
    force_type(user, str)
    fetching = True
    loading_animation = Thread(target = loading)
    loading_animation.start()
    try:
        return requests.get(f"https://replit.com/@{user}").status_code == 200
    finally:
        fetching = False
        loading_animation.join()
