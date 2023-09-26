from calificaciones import *

def main():
    print("Prueba nota teoría")
    print(nota_teoria(9.1, 7.2))
    print(nota_teoria(4.0, 6.0))
    print(nota_teoria(4.0, 3.0))
    print(nota_teoria(None, 3.0))
    print(nota_teoria(9.0, None))

if __name__ == "__main__":
    main()
