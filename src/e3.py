import requests
from utils.common import clear


USERS_URL = "http://packages.educativa.com/samples/usuarios.json"
COURSES_URL = "http://packages.educativa.com/samples/cursos.json"


def fetch(url:str):
    
    res = requests.get(url)
    res.raise_for_status()
    return res.json()


def fetch_users():
    
    return fetch(USERS_URL)["usuarios"]


def fetch_courses():
    
    return fetch(COURSES_URL)["cursos"]


def main():
    
    clear()

    try:
        
        users = fetch_users()
        courses = fetch_courses()
        
        print(f"USUARIOS:\n\n{users}\n\nCURSOS:\n\n{courses}")

    except requests.exceptions.HTTPError as err:

        print(err)


if __name__ == "__main__":
    main()