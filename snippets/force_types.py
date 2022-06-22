from typing import (Any,
                    Callable as Function,
                    List,
                    Dict)
from .Exceptions import (MustBeFunction,
                         ForceType)

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