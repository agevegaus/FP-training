numero = int(input("Ingrese un numero: "))

def esMultiplo(NumeroMayor,NumeroMenor):  # Si el numero mayor es multiplo del menor, devuelve True
    return NumeroMayor%NumeroMenor==0

def esPrimo(num):  # Devuelve True si el parametro es un numero primo
    for iteracion in range(num-1, 1, -1):  # Empieza en i - 1, termina en 2 y decrece de 1 en 1.
        '''
        print(iteracion)
        print(esMultiplo(num,iteracion))
        print("")
        '''

        if (esMultiplo(num,iteracion) == True):
            print("El numero NO es Primo")
            return False

    print("El numero es Primo")
    return True

print(esPrimo(numero))