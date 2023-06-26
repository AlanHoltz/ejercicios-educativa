import argparse
from n1.main import main as exec1
from n2.main import main as exec2
from n3.main import main as exec3
from n4.main import main as exec4


parser = argparse.ArgumentParser(description="CLI de Ejercicios")
parser.add_argument("-e", "--ejercicio", type=int, required=True)
args = parser.parse_args()


numero_ejercicio = vars(args)["ejercicio"]

ejecutar_ejercicio = {1: exec1, 2: exec2, 3: exec3, 4: exec4}[numero_ejercicio]

ejecutar_ejercicio()
