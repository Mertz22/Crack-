import requests
from .force_types import force_type
from .Misc import cursor
from threading import Thread
from time import sleep

fetching = False

def loading() -> None:
    """loading animation for exists fetch function"""
    i = 0
    cursor(0)
    while fetching:
        print(f"fetching data{'.' * i}\r", end="", flush=True)
        sleep(0.5)
        i = (i + 1) % 3
    cursor(1)

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
