from e3 import fetch_usuarios, fetch_cursos
from utils.functions import clear
from utils.db import db_execute_many
from mysql.connector import Error,IntegrityError

    
def fill_table(table_name: str,columns:list, data:list):    
    try:
        rows = []
        for element in data:
            row = tuple([element[column] for column in columns])
            rows.append(row)
        params_to_replace = ','.join(['%s' for i in range(0,len(columns))])
        db_execute_many(f"INSERT INTO {table_name} VALUES ({params_to_replace})", rows)
    except IntegrityError as err:
        print(f"NO SE HA PODIDO CARGAR LOS DATOS EN {table_name}. PROBABLEMENTE LA TABLA YA CONTENGA ALGUNO DE LOS DATOS A INGRESAR.")


def get_users_courses_list(users):
    users_cousers = []
    for user in users:
        user_courses = user["id_curso"]
        for course in user_courses:
            users_cousers.append({"user_id": user["id"], "course_id": course})
    return users_cousers


def main():
    
    clear()

    users = fetch_usuarios()
    courses = fetch_cursos()
    users_courses = get_users_courses_list(users)

    fill_table("usuarios", ["id","nombre", "apellido"], users)
    fill_table("cursos", ["id","nombre","id_docente","cupo"], courses)
    fill_table("usuarios_cursos", ["course_id", "user_id"], users_courses)


if __name__ == "__main__":
    main()