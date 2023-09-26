
def a_cero(nota):
    res = nota
    if nota == None:
        res = 0
    return res

def nota_teoria(nota1, nota2):
    t1 = a_cero(nota1)
    t2 = a_cero(nota2)
    res = (t1 + t2) / 2
    if res < 4:
        res = 0
    return res
