from calificaciones import nota_cuatrimestre, nota_continua, nota_teoria

''' Apartado d
Escribe una función en el módulo 'calificaciones_ui' llamada solicita_notas que solicite por teclado: 
El nombre de un estudiante, las notas de los 4 cuestionarios de teoría y la de los 2 exámenes prácticos y devuelva una tupla con todos los datos leídos (los campos de la tupla deben estar en el mismo orden en el que se han leído). 

Implementa una segunda función llamada mostrar_notas que tome como entrada una tupla con los datos leidos por teclado y los muestre por consola.

En el mismo módulo invoque a estas funciones para solicitar a un usuario sus notas, y mostrarle sus resultados por consola, de la siguiente forma:
Introduzca su nombre: Toñi
Introduzca la nota del examen teórico 1 (- si no se ha presentado):
6.5
Introduzca la nota del examen teórico 2 (- si no se ha presentado):
7.8
Introduzca la nota del examen teórico 3 (- si no se ha presentado):
5.6
Introduzca la nota del examen teórico 4 (- si no se ha presentado):
6.0
Introduzca la nota del examen práctico 1 (- si no se ha presentado):
6.1
Introduzca la nota del examen práctico 2 (- si no se ha presentado):
5.0
Hola, Toñi
Tus notas del primer cuatrimestre son:
 teoria 7.15, práctica 6.1, cuatrimestre 6.3100000000000005
Tus notas del segundo cuatrimestre son:
 teoria 5.8, práctica 5.0, cuatrimestre 5.16
Tu nota final de la asignatura es 5.735
'''

def solicita_notas():
    nombre = input("Introduzca su nombre: ")
    t1 = float(input("Introduzca la nota del examen teórico 1 (- si no se ha presentado): "))
    t2 = float(input("Introduzca la nota del examen teórico 2 (- si no se ha presentado): "))
    t3 = float(input("Introduzca la nota del examen teórico 3 (- si no se ha presentado): "))
    t4 = float(input("Introduzca la nota del examen teórico 4 (- si no se ha presentado): "))
    p1 = float(input("Introduzca la nota del examen práctico 1 (- si no se ha presentado): "))
    p2 = float(input("Introduzca la nota del examen práctico 2 (- si no se ha presentado): "))
    
    return (nombre, t1, t2, t3, t4, p1, p2)

def mostrar_notas(tupla):
    nombre = tupla[0]
    t1 = tupla[1]
    t2 = tupla[2]
    t3 = tupla[3]
    t4 = tupla[4]
    p1 = tupla[5]
    p2 = tupla[6]
    
    print("Hola, " + nombre)
    print("Tus notas del primer cuatrimestre son:")
    print(" teoria " + str(nota_teoria(t1, t2)) + ", práctica " + str(p1) + ", cuatrimestre " + str(nota_cuatrimestre((t1, t2), p1)))
    print("Tus notas del segundo cuatrimestre son:")
    print(" teoria " + str(nota_teoria(t3, t4)) + ", práctica " + str(p2) + ", cuatrimestre " + str(nota_cuatrimestre((t3, t4), p2)))
    print("Tu nota final de la asignatura es " + str(nota_continua((t1, t2, t3, t4), (p1, p2))))

def main():
    mostrar_notas(solicita_notas())

if __name__ == "__main__":
    main()