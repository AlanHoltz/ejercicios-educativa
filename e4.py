from utils.functions import clear
from utils.db import db_execute


def main():

    clear()

    db_execute([
    ("""
    CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_usuario)
    )""",None
    ),
    
    ("""
    CREATE TABLE IF NOT EXISTS cursos(
    id_curso INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,   
    cupo INT UNSIGNED NOT NULL,
    id_docente INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_curso)
    )""",None
    ),
    ("""
    CREATE TABLE IF NOT EXISTS usuarios_cursos(
    id_curso INT UNSIGNED NOT NULL,
    id_alumno INT UNSIGNED NOT NULL,
    PRIMARY KEY (id_curso,id_alumno),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
    FOREIGN KEY (id_alumno) REFERENCES usuarios(id_usuario)
    )""",None
    )
    ])

    print("LAS TABLAS usuarios, cursos y usuarios_cursos HAN SIDO CREADAS CORRECTAMENTE")

    
if __name__ == "__main__":
    main()