import argparse
from dotenv import load_dotenv
from n1.main import main as exec1
from e2 import main as exec2
from n3.main import main as exec3
from e4 import main as exec4
from e5 import main as exec5


load_dotenv()


parser = argparse.ArgumentParser(description="CLI de Ejercicios")
parser.add_argument("-e", "--ejercicio", type=int, required=True)
args = parser.parse_args()


numero_ejercicio = vars(args)["ejercicio"]

ejecutar_ejercicio = {1: exec1, 2: exec2, 3: exec3, 4: exec4, 5:exec5}[numero_ejercicio]

ejecutar_ejercicio()
