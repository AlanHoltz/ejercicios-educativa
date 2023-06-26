from os import getenv
from dotenv import load_dotenv
from mysql.connector import connect, Error as MySQLError


load_dotenv()


def get_db_connection():
    try:
        return connect(
            host="localhost",
            user=getenv("DB_USER"),
            password=getenv("DB_PASSWORD"),
            database="edu_challenge_db"
        )
    except MySQLError as err:
        raise err
    

def statement_is_valid(statement:tuple):
        return len(statement) < 2 or not isinstance(statement[0], str) or not isinstance(statement[1] , (tuple,type(None)))
    

def db_execute(statements:list[tuple]):
    try:
        if not type(statements) == list:
            raise Exception("SE DEBE PROVEER UNA LISTA DE TUPLAS DE LONGITUD 2")
        
        db = get_db_connection()
        cursor = db.cursor()        

        for statement in statements:
            if statement_is_valid(statement):
                raise Exception("LOS ELEMENTOS DE LA LISTA, DEBEN SER UNA TUPLA DE LONGITUD 2, DONDE EL PRIMER ELEMENTO ES UN STRING REPRESENTANDO LA CONSULTA, Y EL SEGUNDO LA TUPLA CON LOS PARÁMETROS (PUEDE SER None)")
            (query,params) = statement
            cursor.execute(query,params)

        db.commit()
        db.close()
    except MySQLError as err:
        raise err