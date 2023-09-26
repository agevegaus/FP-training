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
    print(nota_continua((9.1, 7.2, 9.1, 7.2), (8.1, 8.1)))
    print(nota_continua((4.0, 6.0, 4.0, 6.0), (5.0, 5.0)))
    print(nota_continua((4.0, 3.0, 4.0, 3.0), (None, None)))
    print(nota_continua((None, 3.0, None, 3.0), (None, None)))
    print(nota_continua((9.0, None, 9.0, None), (4.5, 4.5)))

if __name__ == "__main__":
    main()
