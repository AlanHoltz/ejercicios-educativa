import argparse
from utils.db import db_execute
from e5 import listar_inscripciones


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
    if not (parser_values.mostrar or parser_values.inscribir or parser_values.eliminar):
        print("Error: debes ingresar al menos una operación (-m,-i,-e)")
        return False
    if parser_values.mostrar:
        return True
    elif parser_values.usuario is None or parser_values.curso is None:
        print("Error: si ingresa las opciones -i,--inscribir o -e,--eliminar, debe especificar el usuario (-u,--usuario) y el curso (-c,--curso)")
        return False
        

def main():
    parser_values = get_parser_values()
    if not parser_values_are_valid(parser_values):
        return
    pass


if __name__ == "__main__":
    main()