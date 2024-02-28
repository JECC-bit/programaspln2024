import os

carpeta = "Programas\\"
letras = []
simbolos = [",", "(", ")", "/"]
with open(carpeta+"letras.txt", "r") as file:

    lineas = file.readlines()
    lineas = [linea.strip() for linea in lineas]
    
for line in lineas:
    letras.extend(line.split(", "))

print("El contenido del documento es: \n\n", lineas)
input("\n\nPresiona Enter para continuar...")
os.system("cls")


print("El documento separado por comas es: \n\n", letras)
input("\n\nPresiona Enter para continuar...")
os.system("cls")

letras.sort()
print("El documento ordenado es: \n\n", letras)
input("\n\nPresiona Enter para continuar...")
os.system("cls")

for simbolo in simbolos:
    lineas = lineas.replace(simbolo, " " + simbolo + " ")
