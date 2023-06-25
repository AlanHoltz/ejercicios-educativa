from os import system
import platform


def clear():
    if(platform.system() == "Windows"):
        system("cls")
    else:
        system("clear")


def main():

    cadena = "Jacinta_Flores$Juan_Carlos_Feletti$Pedro_Lugones$Ana_María_Galíndez$\
Juana_Bermudez$Rafael_Ernesto_Brahms$Beatriz_Valente$Ulma_Fabiana_Goya$Martina_Nicolesi$\
Betania_Miraflores$Fermín_Olivetti$Ana_Luz_Narosky$Graciana_Arruabarrena$Joel_Pérez$\
Valentina_Feller$Hector_Tadeo_Siemens$Natalia_Martinevsky$Ernesto_Nicolini$Pia_Paez$\
Fermín_Obdulio_Camilo_Galíndez$Delfina_Beirut$Walter_Mantinoli$Celina_Celia_Samid$\
Ulises_Malo$Juana_Varela$Melquíades_José_Li$Radamel_Servini$Filemón_Salsatti$Celeste_Faim$\
Valerio_Martín_Rosseti$Jeremías_Farabutti$Verónica_Nefertiti$Ana_Delia_Pereyra$\
Hermenilda_Carla_Rutini$Valerio_Tunuyán$Silvia_Solano$Beatriz_Bevacqua$Manuel_Martínez$\
Berto_Carlos_Kigali$Juan_Manuel_Miraflores$Nicolás_Kligorsky$María_Laura_Berotti"

    clear()

    cadena = cadena.replace("_"," ")

    cadena = cadena.replace("$"," - ")

    alumnos = cadena.split(" - ")

    for alumno in alumnos:
        print(f"{alumno}\n")


if __name__ == "__main__":
    main()