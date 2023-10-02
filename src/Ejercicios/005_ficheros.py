# Basic
with open("./data/prueba.txt") as fichero:
    for linea in fichero:
        print(linea)

# Encoding
with open("./data/prueba.txt", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea)