"""
As many people have made a lot of python applications in console. However, replit's auth has one major problem: it doesn't work in console so I created this application and you can now securely use replit auth in python console.
- [x] ensures that auth-ed is a person, so this eliminates quite a few problems with people creating fake, non-replit accounts on console apps
- [x] ensures that the person attempting to auth is the person who has authed (no impersonatation)
- [x] thus, you ensure you can only auth as yourself and with banning, you ensure a non-toxic eco-system
- [x] it even includes a cli!

You can fork and make your own server [here](https://replit.com/@bigminiboss/PyAuth-Server-forkable) to integrate into your HTTPS client (uses replit db, replit auth, and replit hosting to create a secure console application auth system and uses replit's linux virtual machine for cursor operation).

Allows you to force types in python as well as add/delete admins, (un)ban, and auth users.
"""

import requests
import os
import sys
from typing import (Callable as Function,
                    Any,
                    List,
                    Dict)
from types import FunctionType

token = None
final_action_executed = False

class AuthFailed(Exception):
    """Exception to be raised when auth fails (timeout, server restart, or 5xx error)"""

class FinalActionExecuted(Exception):
    """Exception for the final action being execute so that nothing else happens"""

class PleaseAuth(Exception):
    """Exception if you have not authed and try to preform an auth action"""

class YouAreNotTheOwner(Exception):
    """Exception if you are not the owner and you try to preform an action in which you need to be owner to preform"""

class MustBeFunction(Exception):
    """Exception if something is not a function but must be"""

class ForceType(Exception):
    """Exception if type should be forced but is not"""

def force_type_pass_function(*args: List[Any], **kwargs: Dict[Any, Any]) -> bool:
    """function for force_type that does nothing"""
    return True

def force_type(variable: Any,
               type_check: Any,
               func_check: Function[..., Any] = force_type_pass_function) -> None:
    """force_type forces a type on a variable"""
    if (not callable(func_check)):
        raise MustBeFunction("\"func_check\" must be callable")
    if (type_check != None and type(variable) != type_check):
        raise ForceType(f"Variable must be type {type_check}")
    if (not func_check(variable)):
        raise ForceType(f"Variable must comply with function check {func_check}")

def exists(user: str) -> bool:
    """returns if user exists on replit"""
    force_type(user, str)
    return requests.get(f"https://replit.com/@{user}").status_code == 200

class Misc:
    """
    Misc Class for some other operations.
    ---------------------------------------
    includes:
        * cursor(type_of_cursor: int)
    """
    def cursor(type_of_cursor: int):
        """
        hide/show/other cursor operations
        -------------------------------
        * 0: hide
        * 1: show

        ----------------------------

        taken from [here](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h4-Functions-using-CSI-_-ordered-by-the-final-character-lparen-s-rparen:CSI-Ps-SP-q.1D81)

        found from [here](https://superuser.com/questions/361335/how-to-change-the-terminal-cursor-from-box-to-line)

        * 2: blinking block
        * 3: default
        * 4: block w/ no blink
        * 5: blinking underline
        * 6: underline w/ no blink
        * 7: blinking bar
        * 8: bar w/ no blink
        """
        # https://superuser.com/questions/361335/how-to-change-the-terminal-cursor-from-box-to-line
        force_type(type_of_cursor, int, lambda x: x in range(9))
        
        mapping = [
            "\033[?25l",
            "\033[?25h",
            "\033[0 q",
            "\033[1 q",
            "\033[2 q",
            "\033[3 q",
            "\033[4 q",
            "\033[5 q",
            "\033[6 q",
        ]
        sys.stdout.write(mapping[type_of_cursor])
        sys.stdout.flush()

def auth_user(url: str = "https://PyAuth-Server.bigminiboss.repl.co",
              user: str = os.environ['REPL_OWNER']) -> None:
    """
    auths user and stores token as a global var for wrapper and security purposes 
    ---------------------------------------------------
    args
        * url: str = "https://PyAuth-Server.bigminiboss.repl.co" (my server)
        * user: str = os.environ["REPL_OWNER"] (current user)
    """    
    global token
    if (token is not None): return
                  
    force_type(url, str)
    force_type(user, str)
    
    id = requests.post(f"{url}/api/auth", json = {
                           "user": user
                       }).text
    
    print(f"please go to {url}/{id}/{user}")
    
    current = requests.get(f"{url}/api/get", json = {
                                   'id': id,
                                   'user': user
                           })
    if (current.status_code == 200):
        token = current.text
    else:
        raise AuthFailed("There was a Timeout (or error, try again)")

def wrapper(auth: bool = True, **kwargs) -> Function[..., Any]:
    """
    main wrapper. You can specify
    --------------------------------------------
    args
       * auth: bool (to before calling function) = False

    kwargs
       * url: str (url that contians PyAuth website) = "https://PyAuth-Server.bigminiboss.repl.co"
       * user: str (user to auth) = os.environ["REPL_OWNER"]
    """
    force_type(auth, bool)
    
    if (final_action_executed):
        raise FinalActionExecuted("The final action was executed. You cannot do anymore actions.")

    def passive() -> None:
        """function that does nothing"""

    def final_action(func: Function[..., Any]) -> None:
        """final action wrapper"""
        global token, final_action_executed
        del token
        final_action_executed = True
        func()
    
    def get_defaults(initial, defaults) -> dict:
        """kwarg defaults"""
        for i in defaults:
            if (i not in initial):
                initial[i] = defaults[i]
        return initial
    kwargs = get_defaults(kwargs, {
        "url": "https://PyAuth-Server.bigminiboss.repl.co",
        "user": os.environ["REPL_OWNER"],
        "end_action": passive,
    })
    force_type(kwargs["url"], str)
    force_type(kwargs["user"], str)
    force_type(kwargs["end_action"], FunctionType)
    
    def wrapper_of_wrapper(func: Function[..., Any]) -> Function[..., Any]:
        """
        specify auth user (you can auth), call func, and delete token
        """
        global token

        force_type(func, FunctionType)
        
        if (auth):
            auth_user(kwargs["url"], kwargs["user"])
        try:
            func()
        finally:
            final_action(kwargs["end_action"])
        return func
    return wrapper_of_wrapper

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