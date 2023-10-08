
# Si nota es None devuelve 0, si no devuelve nota
def a_cero(nota):
    
    res = nota

    if nota == None:
        res = 0.0

    return res


# Hace la media de las notas de teoría y devuelve 0 si es menor que 4 
def nota_teoria(nota1, nota2):

    t1 = a_cero(nota1)
    t2 = a_cero(nota2)
    res = (t1 + t2) / 2

    if res < 4:
        res = 0.0
        
    return res


def nota_cuatrimestre(teoria, practico):
    
    t1 = a_cero(teoria[0])
    t2 = a_cero(teoria[1])
    p1 = a_cero(practico)

    if nota_teoria(t1, t2) >= 4:
        res = (0.1 * t1) + (0.1 * t2) + (0.8 * p1)
    else:
        res = 0.0

    return res


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
