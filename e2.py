from utils.common import clear


def formatear_nombres(lista_nombres:list):       
    for i, nombre_completo in enumerate(lista_nombres):
        nombre = " ".join(nombre_completo.split(" ")[:-1])
        apellido = nombre_completo.split(" ")[-1]
        lista_nombres[i] = f"{apellido}, {nombre}"

    return lista_nombres


def generar_diccionario(lista_nombres:list):
    nombres_dict = {}

    for i in range(1,len(lista_nombres) + 1):
        nombres_dict[i] = lista_nombres[i - 1]

    return nombres_dict


def ordenar(lista_nombres:list):

    lista_nombres = formatear_nombres(lista_nombres)
    
    lista_nombres = sorted(lista_nombres)

    return generar_diccionario(lista_nombres)


def main():
    
    clear()

    lista_nombres = ["Jacinta Flores", "Juan Carlos Feletti","Pedro Lugones", "Ana María Galíndez"]
    
    print(ordenar(lista_nombres))


if __name__ == "__main__":
    main()