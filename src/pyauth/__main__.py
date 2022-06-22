#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# inspired by https://github.com/replit/replit-py/tree/master/src/replit
# put into src/pyauth because https://github.com/replit/replit-py/

import click
from auth import (auth_user,
                  ban,
                  unban,
                  add_admin,
                  delete_admin,
                  exists,
                  Misc,
                  __doc__)
from .get_lines import get_lines
from time import sleep
import os

blue = "\033[34m"
green = "\033[32m"
red = "\033[31m"
end = "\033[0m"
yellow = "\033[33m"

@click.group()
@click.version_option("0.1.0")
def cli() -> None:
    """command line for PyAuth"""

@cli.command(name = "ban")
@click.argument("user")
@click.argument("url", default = "https://PyAuth-Server.bigminiboss.repl.co")
@click.argument("owner", default = os.environ["REPL_OWNER"])
def cli_ban(user: str, url: str, owner: str) -> None:
    """
    \b
    user: str (required)
        user to ban
    url: str = "https://PyAuth-Server.bigminiboss.repl.co" (base server)
        PyAuth server url
    owner: str = current_user
        checks this name with your token against the owner's name and token to make sure it's you or an admin
    """
    auth_user(url, owner)
    ban(user, owner, url)
    click.echo(f"successfully banned user {blue}{user}{end} to url {blue}{url}{end}")

@cli.command(name = "unban")
@click.argument("user")
@click.argument("url", default = "https://PyAuth-Server.bigminiboss.repl.co")
@click.argument("owner", default = os.environ["REPL_OWNER"])
def cli_unban(user: str, url: str, owner: str) -> None:
    """
    \b
    user: str (required)
        user to unban
    url: str = "https://PyAuth-Server.bigminiboss.repl.co" (base server)
        PyAuth server url
    owner: str = current_user
        checks this name with your token against the owner's name and token to make sure it's you or an admin
    """
    auth_user(url, owner)
    unban(user, owner, url)
    click.echo(f"successfully unbanned user {blue}{user}{end} to url {blue}{url}{end}")

@cli.command(name = "exists")
@click.argument("user")
def cli_exists(user: str) -> None:
    """
    \b
    Check if user exists in the replit database
    """
    mapping = [f"an {red}INVALID{end}", f"a {blue}valid{end}"]
    click.echo(f"{user} is {mapping[exists(user)]} user")

@cli.command(name = "add")
@click.argument("user")
@click.argument("url", default = "https://PyAuth-Server.bigminiboss.repl.co")
@click.argument("owner", default = os.environ["REPL_OWNER"])
def cli_add_admin(user: str, url: str, owner: str) -> None:
    """
    \b
    user: str (required)
        user to add to admin database
    url: str = "https://PyAuth-Server.bigminiboss.repl.co" (base server)
        PyAuth server url
    """
    auth_user(url, owner)
    add_admin(user, owner, url)
    click.echo(f"successfully added user {blue}{user}{end} as admin to url {blue}{url}{end}")

@cli.command(name = "delete")
@click.argument("user")
@click.argument("url", default = "https://PyAuth-Server.bigminiboss.repl.co")
@click.argument("owner", default = os.environ["REPL_OWNER"])
def cli_delete_admin(user: str, url: str, owner: str) -> None:
    """
    \b
    user: str (required)
        user to delete from admin database
    url: str = "https://PyAuth-Server.bigminiboss.repl.co" (base server)
        PyAuth server url
    """
    auth_user(url, owner)
    delete_admin(user, owner, url)
    click.echo(f"successfully {red}deleted{end} user {blue}{user}{end} as admin to url {blue}{url}{end}")

@cli.command(name = "auth")
@click.argument("user", default = os.environ["REPL_OWNER"])
@click.argument("url", default = "https://PyAuth-Server.bigminiboss.repl.co")
def cli_auth(user: str, url: str) -> None:
    """
    \b
    user: str (required)
        user to auth
    url: str = "https://PyAuth-Server.bigminiboss.repl.co" (base server)
        PyAuth server url
    """
    auth_user(url, user)
    click.echo(f"{green}successfully{end} authed you!")

@cli.command(name = "cursor")
@click.argument("num", type=int)
def cli_cursor(num: int) -> None:
    """
    \b
    hide/show/other cursor operations
    --------------------------
    * 0: hide
    * 1: show
    
    ----------------------------
    \b
    
    taken from https://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h4-Functions-using-CSI-_-ordered-by-the-final-character-lparen-s-rparen:CSI-Ps-SP-q.1D81
    
    found from https://superuser.com/questions/361335/how-to-change-the-terminal-cursor-from-box-to-line

    \b
    * 2: blinking block
    * 3: default
    * 4: block w/ no blink
    * 5: blinking underline
    * 6: underline w/ no blink
    * 7: blinking bar
    * 8: bar w/ no blink
    """
    Misc.cursor(num)

@cli.command(name = "easter-egg")
def cli_easter_egg() -> None:
    """wow: an easter egg"""
    click.echo(f"PyAuth is {red}awesome{end}! {blue}Easter{end}-{green}egg{end} unlocked!")
    Misc.cursor(0)
    for i in range(18):
        click.echo(f"you got{'.' * (i % 4)}   \r", nl="")
        sleep(0.15)
    Misc.cursor(1)
    click.echo(f"{blue}the prior was just an {red}animation{end}{blue}, it was {red}not{end}{blue} doing anything{end}\nA docstring!\n{__doc__}", nl="")

@cli.command(name = "get-lines")
@click.option('-q', is_flag = True, help = "whether or not to output the file locations of the files used to write this code")
def cli_get_lines(q: bool) -> None:
    """
    see how many lines were used to create this project
    """
    click.echo(f"this project used {green}{get_lines(os.getcwd(), q, click.echo) + get_lines(os.getcwd() + '/src/pyauth', q, click.echo)}{end} lines of code!")

@cli.command(name = "clear")
def cli_clear():
    """clear screen"""
    click.echo("\033c", nl="")

if (__name__ == "__main__"):
    cli(prog_name = "pyauth")