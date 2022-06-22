import auth
import os

# auths and then calls function specified function under decorater
# auth: bool = True (default): will auth
# url: str = "https://PyAuth-Server.bigminiboss.repl.co" (default)
# user: str = os.environ["REPL_OWNER"] (default)
@auth.wrapper(auth = True,
              url = "https://PyAuth-Server.bigminiboss.repl.co",
              user = os.environ["REPL_OWNER"])
def main():
    # auth.token is deleted when you use the wrapper for safety.
    print("Your token is", auth.token)