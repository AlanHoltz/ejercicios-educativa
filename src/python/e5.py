from e3 import fetch_users, fetch_courses
from utils.common import clear
from utils.db import db_execute_many, db_execute
from mysql.connector import IntegrityError, Error as MySQLError
from tabulate import tabulate


def get_enrollments(users:list):
    
    enrollments = []
    for user in users:
        user_courses = user["id_curso"]
        for course in user_courses:
            enrollments.append({"user_id": user["id"], "course_id": course})
    return enrollments

        
def fill_table(table_name: str,columns:list, data:list):    
    
    try:
        rows = []
        for element in data:
            row = tuple([element[column] for column in columns])
            rows.append(row)
        params_to_replace = ','.join(['%s' for i in range(0,len(columns))])
        db_execute_many(f"INSERT INTO {table_name} VALUES ({params_to_replace})", rows)
    except IntegrityError:
        pass
    except MySQLError as err:
        print(err)


def show_enrollments():

    joined_tables = db_execute("""
    SELECT 
    uc.id_alumno,uc.id_curso,
    CONCAT(u.nombre," ",u.apellido) AS "nombre y apellido usuario",
    c.nombre 
    FROM usuarios_cursos uc
    INNER JOIN usuarios u ON u.id_usuario = uc.id_alumno
    INNER JOIN cursos c ON c.id_curso = uc.id_curso
    """)

    print("LISTADO DE INSCRIPCIONES\n")
    print(tabulate(joined_tables, ["id_usuario","id_curso","nombre y apellido usuario","nombre curso"], tablefmt="github"))


def main():
    
    clear()

    users = fetch_users()
    courses = fetch_courses()
    enrollments = get_enrollments(users)

    fill_table("usuarios", ["id","nombre", "apellido"], users)
    fill_table("cursos", ["id","nombre","cupo","id_docente"], courses)
    fill_table("usuarios_cursos", ["course_id", "user_id"], enrollments)

    show_enrollments()


if __name__ == "__main__":
    main()