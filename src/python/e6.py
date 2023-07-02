import argparse
from utils.db import db_execute
from e5 import show_enrollments
from utils.common import clear


def get_parser_values():
    
    parser = argparse.ArgumentParser(add_help=False)
    operations = parser.add_mutually_exclusive_group()
    parser.add_argument('-h', '--help' , action='help',default=argparse.SUPPRESS,help="Muestra este mensaje")
    operations.add_argument('-m','--mostrar', dest="show",help="Mostrar lista de inscripciones", action="store_true")
    operations.add_argument('-i', '--inscribir', dest="enroll",help="Inscribir", action="store_true")
    operations.add_argument('-e', '--eliminar',dest="delete",help="Eliminar", action="store_true")
    parser.add_argument('-u', '--usuario',dest="user",help="Usuario a inscribir/eliminar de una inscripción", type=int)
    parser.add_argument('-c', '--curso',dest="course",help="Curso donde inscribir/eliminar la inscripción del usuario", type=int)

    args = parser.parse_args()

    if not any(vars(args).values()):
        return parser.print_help()

    return args


def parser_values_are_valid(parser_values):

    at_least_one_operation = parser_values.show or parser_values.enroll or parser_values.delete 

    if not at_least_one_operation:
        print("Error: debes ingresar al menos una operación (-m,-i,-e)")
        return False
    
    user_and_course_defined = not(parser_values.user is None or parser_values.course is None) 

    if not parser_values.show and not user_and_course_defined:
        print("Error: si ingresa las opciones -i,--inscribir o -e,--eliminar, debe especificar el usuario (-u,--usuario) y el curso (-c,--curso)")
        return False

    return True


def create_enrollment(user,course):

    [student_id,student_name,student_surname] = user[0]
    [course_id,course_name] = course[0][:2]
    
    db_execute("INSERT INTO usuarios_cursos VALUES (%s,%s)",[course_id, student_id])
    print(f"SE HA INSCRIPTO AL USUARIO {student_name} {student_surname} (ID: {student_id}) AL CURSO {course_name} (ID: {course_id})")


def delete_enrollment(user,course):

    [student_id,student_name,student_surname] = user[0]
    [course_id,course_name] = course[0][:2]

    db_execute("DELETE FROM usuarios_cursos WHERE id_curso = %s AND id_alumno = %s", [course_id, student_id])
    print(f"SE HA ELIMINADO LA INSCRIPCIÓN DEL USUARIO {student_name} {student_surname} (ID: {student_id}) AL CURSO {course_name} (ID: {course_id})")


def get_user(parser_values):
    
    return db_execute("SELECT * FROM usuarios u WHERE u.id_usuario = %s", [parser_values.user])


def get_course(parser_values):
    
    return db_execute("SELECT * FROM cursos u WHERE u.id_curso = %s", [parser_values.course])


def user_and_course_values_are_valid(user,course):

    student_id = user[0][0]
    course_id = course[0][0]
    
    if not any(user):
        print(f"EL USUARIO DE ID {student_id} NO EXISTE")
        return False 
    
    if not any(course):
        print(f"EL CURSO DE ID {course_id} NO EXISTE")  
        return False
    
    return True
    

def existing_enrollment(user,course):
    
    [student_id,student_name,student_surname] = user[0]
    [course_id,course_name] = course[0][:2]

    enrollment = db_execute("SELECT * FROM usuarios_cursos WHERE id_alumno = %s AND id_curso = %s", [student_id, course_id])
    if any(enrollment):
        print(f"YA EXISTE UNA INSCRIPCIÓN DEL USUARIO {student_name} {student_surname} (ID: {student_id}) AL CURSO {course_name} (ID: {course_id})")
        return True 
    
    return False
        

def main():

    parser_values = get_parser_values()

    if parser_values is None or not parser_values_are_valid(parser_values):
        return
       
    if parser_values.show:
        show_enrollments()
        
    else:

        user = get_user(parser_values)
        course = get_course(parser_values)

        if not user_and_course_values_are_valid(user,course):
            return

        if parser_values.enroll and not existing_enrollment(user,course):
            create_enrollment(user, course)
        elif parser_values.delete:
            delete_enrollment(user, course)


if __name__ == "__main__":
    main()