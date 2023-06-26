import requests
from utils.functions import clear


USUARIOS_URL = "http://packages.educativa.com/samples/usuarios.json"
CURSOS_URL = "http://packages.educativa.com/samples/cursos.json"


def fetch(url):
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


def fetch_usuarios():
    return fetch(USUARIOS_URL)


def fetch_cursos():
    return fetch(CURSOS_URL)


def main():
    
    clear()

    try:
        
        usuarios = fetch_usuarios()
        cursos = fetch_cursos()
        print(f"USUARIOS:\n\n{usuarios['usuarios']}\n\nCURSOS:\n\n{cursos['cursos']}")

    except requests.exceptions.HTTPError as err:
        print(err)


if __name__ == "__main__":
    main()