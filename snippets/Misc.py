from .force_types import force_type
from typing import Tuple
import sys

def must_be_of_strings(obj):
    """Must be tuple of strings"""
    for i in obj:
        if (type(i) != str): return False
    return True

def cursor(type_of_cursor: int):
    """
    hide/show/other cursor operations
    --------------------------
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

def typer(*words: Tuple[str], end: str="\n", sep: str="") -> None:
    """typer writer effect"""
    force_type(words, tuple, must_be_of_strings)
    force_type(end, str)
    force_type(sep)
    for i in sep.join(words) + end:
        sys.stdout.write(i)
        sys.stdout.flush()

class Clear:
    """clear screen utils"""
    def __call__(self) -> None:
        """clear screen"""
        print("\033c", end="", flush=True)

clear = Clear()