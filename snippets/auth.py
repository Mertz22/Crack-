
import os
import requests
from .force_types import force_type
from .Exceptions import AuthFailed

token = None
final_action_executed = False

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