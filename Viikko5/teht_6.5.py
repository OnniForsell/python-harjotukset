def poista(lukuja):
    lista = []
    for n in luvut:
        if n % 2 == 0:
            lista.append(n)
    return lista

luvut = [1, 2, 3, 8, 5, 6, 11, 14, 16, 19, 20]
print(luvut)
print(poista(luvut))