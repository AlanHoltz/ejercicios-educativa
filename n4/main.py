from utils.functions import clear
from mysql.connector import connect, Error
from os import getenv
from dotenv import load_dotenv


load_dotenv()


def get_db_connection():
    try:
        return connect(
            host="localhost",
            user=getenv("DB_USER"),
            password=getenv("DB_PASSWORD"),
            database="edu_challenge_db"
        )
    except Error as err:
        print(err)


def execute(query, params=None):
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        db.close()
    except Error as err:
        print(err)


def main():

    clear()

    execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INT UNSIGNED NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_usuario)
    )
    """)

    execute("""
    CREATE TABLE IF NOT EXISTS cursos(
    id_curso INT UNSIGNED NOT NULL,
    nombre VARCHAR(255) NOT NULL,   
    cupo INT UNSIGNED NOT NULL,
    id_docente INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_curso),
    FOREIGN KEY (id_docente) REFERENCES usuarios(id_usuario)
    )
    """)


    execute("""
    CREATE TABLE IF NOT EXISTS usuarios_cursos(
    id_curso INT UNSIGNED NOT NULL,
    id_alumno INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_curso,id_alumno),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
    FOREIGN KEY (id_alumno) REFERENCES usuarios(id_usuario)
    )
    """)

    print("LAS TABLAS usuarios, cursos y usuarios_cursos HAN SIDO CREADAS CORRECTAMENTE")