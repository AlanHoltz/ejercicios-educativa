import requests
from utils.common import clear


USUARIOS_URL = "http://packages.educativa.com/samples/usuarios.json"
CURSOS_URL = "http://packages.educativa.com/samples/cursos.json"


def fetch(url:str):
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


def fetch_usuarios():
    return fetch(USUARIOS_URL)["usuarios"]


def fetch_cursos():
    return fetch(CURSOS_URL)["cursos"]


def main():
    
    clear()

    try:
        
        usuarios = fetch_usuarios()
        cursos = fetch_cursos()
        
        print(f"USUARIOS:\n\n{usuarios}\n\nCURSOS:\n\n{cursos}")

    except requests.exceptions.HTTPError as err:
        print(err)


if __name__ == "__main__":
    main()