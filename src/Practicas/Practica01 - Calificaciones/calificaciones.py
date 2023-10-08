
# Si nota es None devuelve 0, si no devuelve nota
def a_cero(nota):
    
    res = nota

    if nota == None:
        res = 0.0

    return res

''' Apartado a
Escribe una función en el módulo 'calificaciones' llamada nota_teoria que, dadas las notas de los dos exámenes teóricos de un cuatrimestre, permita calcular la nota que un alumno tiene en el bloque teórico de ese cuatrimestre. 

La nota se calcula como la media de las notas de ambos cuatrimestres. Una nota con valor None indica que el alumno no se ha presentado al examen, y se considerará como un cero.

Pruebas: Pruebe la función en el módulo calificaciones_test con los siguientes valores, siendo los dos números que están antes de la flecha las notas del primer y segundo exámen teórico, respectivamente, y el valor situado a la derecha de la flecha la nota obtenida.
9.1, 7.2 ==> 8.15
4.0, 6.0 ==> 5.0
4.0, 3.0 ==> 3.5
None, 3.0 ==>1.5
9.0, None ==> 4.5
'''
# Hace la media de las notas de teoría y devuelve 0 si dicha media es menor que 4 
def nota_teoria(nota1, nota2):

    t1 = a_cero(nota1)
    t2 = a_cero(nota2)
    res = (t1 + t2) / 2

    if res < 4:
        res = 0.0
        
    return res

''' Apartado b
Escribe una función en el módulo 'calificaciones' llamada nota_cuatrimestre que, dadas una tupla con dos elementos (las notas de los exámenes teóricos de un cuatrimestre), y la nota del exámen práctico, devuelva la nota obtenida en ese cuatrimestre. 

La nota del cuatrimestre, siempre que la media de los dos cuestionarios teóricos sea superior o igual a 4, se calcula como 0,1* (T1+T2) + 0,8 * P, siendo T1 y T2 las notas de los dos exámenes teóricos y P la nota del examen práctico. 

Si la media no es superior a 4, la nota del cuatrimestre es 0. 

Un valor None en una nota indica que el alumno no se ha presentado al examen, y se considerará como un cero.

Pruebas: Pruebe la función en el módulo calificaciones_test con los siguientes valores, siendo los números situados a la izquierda de la flecha las notas del primer examen teórico, del segundo y del examen práctico, respectivamente. 
La nota obtenida es el número situado a la derecha de la flecha.
9.1, 7.2, 8.1 ==> 8.110000000000001
4.0, 6.0, 5.0 ==> 5.0
4.0, 3.0, None ==> 0
None, 3.0, None  ==>0
9.0, None, 4.5 ==> 4.5
'''
def nota_cuatrimestre(teoria, practico):
    
    t1 = a_cero(teoria[0])
    t2 = a_cero(teoria[1])
    p1 = a_cero(practico)

    if nota_teoria(t1, t2) >= 4:
        res = (0.1 * t1) + (0.1 * t2) + (0.8 * p1)
    else:
        res = 0.0

    return res

''' Apartado c
Escribe una función en el módulo 'calificaciones' llamada nota_continua que, dadas una tupla con las notas de los 4 exámenes teóricos del curso, y otra tupla con la nota de los dos exámenes prácticos, devuelva la nota obtenida por evaluación continua. 

La nota de la evaluación continua se calcula como la media de las notas de los dos cuatrimestres, siempre que la nota de ambos cuatrimestres sea superior a 4. 

Si en alguno de los dos cuatrimestres la nota es inferior a 4, entonces la nota es el mínimo entre 4 y la nota media de los cuatrimestres. 

El valor None en una nota indica que el alumno no se ha presentado al examen, y se considerará como cero.

Pruebas: Pruebe la función en el módulo calificaciones_test con los siguientes valores, siendo los números situados a la izquierda de la flecha las notas del primer examen teórico, del segundo y del examen práctico, respectivamente. 
La nota obtenida es el número situado a la derecha de la flecha.
    notas teoría:  9.6, 9.9,10.0, 9.8 notas_práctico: 9.7,9.5 ==> 9.645
    notas teoría: 4.4, 4.9, 5.1, 4.7 notas_práctico: 4.6,4.8 ==> 4.715
    notas teoría: 4.0, 6.0, 4.0, 3.0 notas_práctico: 5.0, None ==> 2.5
    notas teoría: 9.0, None, 4.0, 3.0 notas_práctico: 4.5, None ==> 2.25
'''
def nota_continua(tupla_teoricos, tupla_practicos):

    t1 = a_cero(tupla_teoricos[0])
    t2 = a_cero(tupla_teoricos[1])
    t3 = a_cero(tupla_teoricos[2])
    t4 = a_cero(tupla_teoricos[3])
    p1 = a_cero(tupla_practicos[0])
    p2 = a_cero(tupla_practicos[1])

    c1 = nota_cuatrimestre((t1, t2), p1)
    c2 = nota_cuatrimestre((t3, t4), p2)

    if c1 >= 4 and c2 >= 4:
        res = (c1 + c2) / 2
    else:
        res = min(4, (c1 + c2) / 2)

    return res
