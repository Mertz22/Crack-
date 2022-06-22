import requests
from .force_types import force_type
from threading import Thread
from time import sleep

fetching = False

def loading():
    """loading animation for exists fetch function"""
    i = 0
    while fetching:
        i = (i + 1) % 3
        print(f"\033cfetching data{'.' * i}", end="")
        sleep(0.05)
    print("\033c", end="")

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
