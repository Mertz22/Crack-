import os
output = 0

def recursive(path, quiet=False):
    global output
    for i in os.listdir(path):
        if (os.path.isdir(i)):
            get_lines(f"{path}/{i}", quiet)
        if (i.endswith(".py")):
            amount = len(open(f"{path}/{i}").read().split('\n'))
            output += amount
            if (not quiet):
                print(f"{path}/{i} ({amount} lines)")

def get_lines(path, quiet = False):
    recursive(path, quiet)
    return output