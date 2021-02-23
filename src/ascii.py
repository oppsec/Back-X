from rich import print

def get_ascii():
    with open('src/ascii.txt', encoding='utf-8') as file:
        content = file.read()
        print(f"[blue]{content} [/]")
