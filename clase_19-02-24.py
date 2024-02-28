import os
import re

######################################################################## Uso de replace
carpeta = "Programas\\"
letras = []
simbolos = [",", "(", ")", "/"]
with open(carpeta+"letras.txt", "r") as file:

    lineas = file.read()

# for simbolo in simbolos:
#     lineas = lineas.replace(simbolo, " ")

# nuevaLinea = lineas.split()
# nuevaLinea.sort()
# print(nuevaLinea)
########################################################################

######################################################################## Uso de expresiones regulares
exp_re = re.compile(r"ll*")
resultado = exp_re.finditer(lineas)

for dato in resultado:
    print(f"Si existe la palabra {dato.group(0)}")
