import os
import requests
from .force_types import force_type
from .auth import final_action_executed, token
from .Exceptions import (YouAreNotTheOwner,
                        PleaseAuth,
                        FinalActionExecuted)

def ban(to_ban: str,
        owner: str = os.environ['REPL_OWNER'],
        url: str = "https://PyAuth-Server.bigminiboss.repl.co") -> None:
    """
    Ban a user IF you are the owner or are an admin and you are authed. For this operation please fork [here](https://replit.com/@bigminiboss/PyAuth-Server-forkable?v=1) and fill out YOUR_USER_NAME_HERE
    ---------------------------------------
    args
        * to_ban: str (user to ban)
        * owner: str (this is your username for auth -- only the owner/admins is allowed to ban)
        * url: str (pyauth server)
    """
    force_type(to_ban, str)
    force_type(owner, str)
    force_type(url, str)
    
    if (not final_action_executed and token is not None):
        status_code = requests.delete(f"{url}/api/ban", json = {
                "user": owner,
                "token": token,
                "ban": to_ban
        }).status_code
        if (status_code == 200):
            return status_code
        elif (status_code == 400):
            raise YouAreNotTheOwner("You are not the owner/admin")
    elif (token is None):
        raise PleaseAuth("Please Auth before doing this action")
    else:
        raise FinalActionExecuted("The final action was already executed")

def unban(to_unban: str,
          owner: str = os.environ['REPL_OWNER'],
          url: str = "https://PyAuth-Server.bigminiboss.repl.co") -> None:
    """
    Unban a user IF you are the owner or an admin and you are authed. For this operation please fork [here](https://replit.com/@bigminiboss/PyAuth-Server-forkable?v=1) and fill out YOUR_USER_NAME_HERE
    ---------------------------------------
    args
        * to_unban: str (user to unban)
        * owner: str (this is your username for auth -- only the owner/admins is allowed to unban)
        * url: str (pyauth server)
    """
    force_type(to_unban, str)
    force_type(owner, str)
    force_type(url, str)
    
    if (not final_action_executed and token is not None):
        status_code = requests.post(f"{url}/api/unban", json = {
                "user": owner,
                "token": token,
                "unban": to_unban
        }).status_code
        if (status_code == 200):
            return status_code
        elif (status_code == 400):
            raise YouAreNotTheOwner("You are not the owner/admin")
    elif (token is None):
        raise PleaseAuth("Please Auth before doing this action")
    else:
        raise FinalActionExecuted("The final action was already executed")

def add_admin(to_add: str,
              owner: str = os.environ['REPL_OWNER'],
              url: str = "https://PyAuth-Server.bigminiboss.repl.co") -> None:
    """
    add an admin IF you are the owner and you are authed. For this operation please fork [here](https://replit.com/@bigminiboss/PyAuth-Server-forkable?v=1) and fill out YOUR_USER_NAME_HERE
    ---------------------------------------
    args
        * to_add: str (user to add as admin)
        * owner: str (this is your username for auth -- only the owner is allowed to add admin)
        * url: str (pyauth server)
    """
    force_type(to_add, str)
    force_type(owner, str)
    force_type(url, str)

    if (not final_action_executed and token is not None):
        status_code = requests.post(f"{url}/api/add_admin", json = {
                "user": owner,
                "token": token,
                "add": to_add
        }).status_code
        if (status_code == 200):
            return status_code
        elif (status_code == 400):
            raise YouAreNotTheOwner("You are not the owner/admin")
    elif (token is None):
        raise PleaseAuth("Please Auth before doing this action")
    else:
        raise FinalActionExecuted("The final action was already executed")

def delete_admin(to_delete: str,
                 owner: str = os.environ['REPL_OWNER'],
                 url: str = "https://PyAuth-Server.bigminiboss.repl.co") -> None:
    """
    delete an admin IF you are the owner and you are authed. For this operation please fork [here](https://replit.com/@bigminiboss/PyAuth-Server-forkable?v=1) and fill out YOUR_USER_NAME_HERE
    ---------------------------------------
    args
        * to_delete: str (user to delete admin)
        * owner: str (this is your username for auth -- only the owner is allowed to delete admin)
        * url: str (pyauth server)
    """
    force_type(to_delete, str)
    force_type(owner, str)
    force_type(url, str)

    if (not final_action_executed and token is not None):
        status_code = requests.delete(f"{url}/api/delete_admin", json = {
                "user": owner,
                "token": token,
                "delete": to_delete
        }).status_code
        if (status_code == 200):
            return status_code
        elif (status_code == 400):
            raise YouAreNotTheOwner("You are not the owner/admin")
    elif (token is None):
        raise PleaseAuth("Please Auth before doing this action")
    else:
        raise FinalActionExecuted("The final action was already executed")