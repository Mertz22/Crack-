import os
output = 0

def recursive(path, quiet=False, printer = print):
    """
    recursively retrieve lines
    """
    global output
    for i in os.listdir(path):
        if (os.path.isdir(i)):
            get_lines(f"{path}/{i}", quiet, printer)
        if (i.endswith(".py") or i.endswith(".py_") or i.endswith('.md')):
            amount = len(open(f"{path}/{i}").read().split('\n'))
            output += amount
            if (not quiet):
                printer(f"{path}/{i} ({amount} lines)")

def get_lines(path, quiet = False, printer = print):
    """
    wrapper since it uses globals
    """
    recursive(path, quiet, printer)
    return output