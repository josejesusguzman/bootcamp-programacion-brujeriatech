# argpase
# Análisis de argumentos de linea de comandos
"""
Analizar argumentos y opciones de linea de comandos.
Para crear scripts en python
"""

# Biblioteca estandar de python. ya no tienes que hacer el pip install
# Son cosas que ya tiene el lenguaje

import argparse

parser = argparse.ArgumentParser(description="Procesa algunos enteros")
parser.add_argument('enteros', metavar='Num', type=int, nargs='+', help="un entero para sumarlo en el acumulador")

parser.add_argument('--sum', dest="accumulate", action="store_const", const=sum, default=max, help="suma de enteros")

args = parser.parse_args()

print(args.accumulate(args.enteros))