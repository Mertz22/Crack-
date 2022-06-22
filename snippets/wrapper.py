from typing import Callable as Function, Any
from types import FunctionType
from .force_types import force_type
from .Exceptions import FinalActionExecuted
from .auth import (auth_user,
                   token,
                   final_action_executed)
import os

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