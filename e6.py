import argparse
from utils.db import db_execute
from e5 import listar_inscripciones
from utils.common import clear


def get_parser_values():
    parser = argparse.ArgumentParser(add_help=False)
    operations = parser.add_mutually_exclusive_group()
    parser.add_argument('-h', '--help' , action='help',default=argparse.SUPPRESS,help="Muestra este mensaje")
    operations.add_argument('-m','--mostrar',help="Mostrar lista de inscripciones", action="store_true")
    operations.add_argument('-i', '--inscribir',help="Inscribir", action="store_true")
    operations.add_argument('-e', '--eliminar',help="Eliminar", action="store_true")
    parser.add_argument('-u', '--usuario',help="Usuario a inscribir/eliminar de una inscripción", type=int)
    parser.add_argument('-c', '--curso',help="Curso donde inscribir/eliminar la inscripción del usuario", type=int)

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()

    return args


def parser_values_are_valid(parser_values):

    at_least_one_operation = parser_values.mostrar or parser_values.inscribir or parser_values.eliminar 

    if not (at_least_one_operation):
        print("Error: debes ingresar al menos una operación (-m,-i,-e)")
        return False
    
    user_and_course_defined = not(parser_values.usuario is None or parser_values.curso is None) 

    if not parser_values.mostrar and not user_and_course_defined:
        print("Error: si ingresa las opciones -i,--inscribir o -e,--eliminar, debe especificar el usuario (-u,--usuario) y el curso (-c,--curso)")
        return False

    return True


def user_and_course_values_are_valid(parser_values):

    usuario = db_execute("SELECT * FROM usuarios u WHERE u.id_usuario = %s", [parser_values.usuario])
    if not any(usuario):
        print(f"EL USUARIO DE ID {parser_values.usuario} NO EXISTE")
        return False 
    
    curso = db_execute("SELECT * FROM cursos u WHERE u.id_curso = %s", [parser_values.curso])
    if not any(curso):
        print(f"EL CURSO DE ID {parser_values.curso} NO EXISTE")  
        return False
    
    return True
    

def existing_enrollment(parser_values):

    enrollment = db_execute("SELECT * FROM usuarios_cursos WHERE id_alumno = %s AND id_curso = %s", [parser_values.usuario, parser_values.curso])
    if any(enrollment):
        print(f"YA EXISTE UNA INSCRIPCIÓN DEL USUARIO CON ID {parser_values.usuario} AL CURSO DE ID {parser_values.curso}")
        return True 
    
    return False


def inscribir_usuario_a_curso(parser_values):
    
    if user_and_course_values_are_valid(parser_values) and not existing_enrollment(parser_values):
        db_execute("INSERT INTO usuarios_cursos VALUES (%s,%s)",[parser_values.curso, parser_values.usuario])
        print(f"SE HA INSCRIPTO AL USUARIO CON ID {parser_values.usuario} AL CURSO DE ID {parser_values.curso}")


def eliminar_usuario_de_curso(parser_values):
    if user_and_course_values_are_valid(parser_values):
        db_execute("DELETE FROM usuarios_cursos WHERE id_curso = %s AND id_alumno = %s", [parser_values.curso, parser_values.usuario])
        print(f"SE HA ELIMINADO LA INSCRIPCIÓN DEL USUARIO CON ID {parser_values.usuario} AL CURSO DE ID {parser_values.curso}")
        

def main():

    parser_values = get_parser_values()
       
    if not parser_values_are_valid(parser_values):
        return
    
    if parser_values.mostrar:
        listar_inscripciones()
        
    elif parser_values.inscribir:
        inscribir_usuario_a_curso(parser_values)
    
    else:
        eliminar_usuario_de_curso(parser_values)


if __name__ == "__main__":
    main()