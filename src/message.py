from rich import print

def success(message):
    return print(f"[green][*] {message} [/]")

def error(message):
    return print(f"[red][!] {message} [/]")

def warn(message):
    return print(f"[yellow][-] {message} [/]")

