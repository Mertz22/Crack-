"""
Wow! this project has come so far from the side project to add replit auth to console to a full fledged 2500+ (including markdown & server code) lines project!
It's truly a labor of love from the built in replit-py styled command line to the meticulously labeled docstrings to the superbly crafted and ease-of-use functions!
The project is a replit auth solution for console with the server being housed at [PyAuth Server](https://PyAuth-Server.bigminiboss.repl.co) and the [forkable version here](https://PyAuth-Server-forkable.bigminiboss.repl.co)
It uses uses replit db, replit auth, and replit hosting to create a secure console application auth system and uses replit's linux virtual machine for cursor operation as well as itsdangerous for hashing.
This is for the replit template jam, recieving enough accolades would allow me to improve it much more (allowing me to confer with people on the homepage of the repl)
"""

import auth
import os

# Exerpt
print(__doc__.strip(),
      "thanks for listening!",
      "Cheers,",
      "bigminiboss", 
      sep="\n",
      end="\n\n")

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