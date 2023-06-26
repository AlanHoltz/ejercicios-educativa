import platform
from os import system


def clear():
    if(platform.system() == "Windows"):
        system("cls")
    else:
        system("clear")