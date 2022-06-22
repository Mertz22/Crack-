from .force_types import force_type
import sys

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