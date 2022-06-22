import requests
from .force_types import force_type

def exists(user: str) -> bool:
    """returns if user exists on replit"""
    force_type(user, str)
    return requests.get(f"https://replit.com/@{user}").status_code == 200