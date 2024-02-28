import re

carpeta = "Programas\\"
with open(carpeta+"cuento.txt", "r") as file:

    lineas2 = file.read()

exp_re2 = re.compile(r"(el)?(la)? farero?")
resultado2 = exp_re2.finditer(lineas2)

for dato2 in resultado2:
    print(f"Si existe la palabra: {dato2.group(0)}")

with open(carpeta+"datos.txt", "r") as file:

    lineas = file.read()

exp_re = re.compile(r"\d+(,\d+)*(\.\d+)?")
resultado = exp_re.finditer(lineas)

for dato in resultado:
    print(f"Si existe el numero: {dato.group(0)}")