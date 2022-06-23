"""
Wow! this project has come so far from the side project to add replit auth to console toa full fledged 2100+ lines project!
It's truly a labor of love from the built in replit-db sytled command line to the meticulously labeled docstrings to the superbly crafted and ease-of-use functions!
The project is a replit auth solution for console with the server being housed at https://PyAuth-Server.bigminiboss.repl.co and the forkable version here https://PyAuth-Server-forkable.bigminiboss.repl.co
It uses uses replit db, replit auth, and replit hosting to create a secure console application auth system and uses replit's linux virtual machine for cursor operation.
If I win achieve a high enough position, I will likely be able to confer with replit to increase user experience on the homepage of this repl!
"""

import auth
import os

# Exerpt
print(__doc__.lstrip(), "thanks for listening!", "Cheers,", "bigminiboss", sep="\n", end="\n\n")

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