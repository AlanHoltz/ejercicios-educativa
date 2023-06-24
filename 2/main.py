from os import system
import platform


def clear():
    if (platform.system() == "Windows"):
        system("cls")
    else:
        system("clear")


def formatear_nombres(lista_nombres):       
    for i, nombre_completo in enumerate(lista_nombres):
        nombre = " ".join(nombre_completo.split(" ")[:-1])
        apellido = nombre_completo.split(" ")[-1]
        lista_nombres[i] = f"{apellido}, {nombre}"

    return lista_nombres


def generar_diccionario(lista_nombres):
    nombres_dict = {}

    for i in range(1,len(lista_nombres) + 1):
        nombres_dict[i] = lista_nombres[i - 1]

    return nombres_dict


def ordenar(lista_nombres):

    lista_nombres = formatear_nombres(lista_nombres) #SE FORMATEAN LOS NOMBRES COMPLETOS DE LA SIGUIENTE MANERA: Apellido, Nombre
    
    lista_nombres = sorted(lista_nombres) # SE ORDENAN LOS NOMBRES ALFABÉTICAMENTE POR APELLIDO

    return generar_diccionario(lista_nombres)


def main():
    
    clear()

    lista_nombres = ["Jacinta Flores", "Juan Carlos Feletti","Pedro Lugones", "Ana María Galíndez"]
    
    print(ordenar(lista_nombres))


if __name__ == "__main__":
    main()