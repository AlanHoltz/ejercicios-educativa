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
        

def db_execute(query:str,params:list=None):
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(query,params)
        data = cursor.fetchall()
        db.commit()
        return data
    except MySQLError as err:
        raise err
    finally:
        cursor.close()
        db.close()
        

def db_execute_many(query:str,rows:list[tuple]):
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.executemany(query, rows)
        db.commit()
    except MySQLError as err:
        raise err
    finally:
        cursor.close()
        db.close()