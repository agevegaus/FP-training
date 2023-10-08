from calificaciones import *

def main():
    print("Pruebas nota teoría")
    print(nota_teoria(9.1, 7.2))
    print(nota_teoria(4.0, 6.0))
    print(nota_teoria(4.0, 3.0))
    print(nota_teoria(None, 3.0))
    print(nota_teoria(9.0, None))

    print("Pruebas nota cuatrimestre")
    print(nota_cuatrimestre((9.1, 7.2), 8.1))
    print(nota_cuatrimestre((4.0, 6.0), 5.0))
    print(nota_cuatrimestre((4.0, 3.0), None))
    print(nota_cuatrimestre((None, 3.0), None))
    print(nota_cuatrimestre((9.0, None), 4.5))

    print("Pruebas nota continua")
    print(nota_continua((9.6, 9.9, 10.0, 9.8), (9.7, 9.5)))
    print(nota_continua((4.4, 4.9, 5.1, 4.7), (4.6, 4.8)))
    print(nota_continua((4.0, 6.0, 4.0, 3.0), (5.0, None)))
    print(nota_continua((9.0, None, 4.0, 3.0), (4.5, None)))

if __name__ == "__main__":
    main()
