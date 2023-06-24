import platform
from os import system
import requests


def clear():
    if (platform.system() == "Windows"):
        system("cls")
    else:
        system("clear")


def fetch(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except requests.exceptions.HTTPError as err:
        raise err


def main():
    
    clear()

    try:
        
        usuarios = fetch("http://packages.educativa.com/samples/usuarios.json")
        cursos = fetch("http://packages.educativa.com/samples/cursos.json")
        print(f"USUARIOS:\n\n{usuarios['usuarios']}\n\nCURSOS:\n\n{cursos['cursos']}")

    except requests.exceptions.HTTPError as err:
        print(err)


if __name__ == "__main__":
    main()

#pip install requests