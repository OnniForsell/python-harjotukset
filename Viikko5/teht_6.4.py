def luoLista(lukuja):
    lukulista = lukuja
    num = 0
    for n in lukulista:
        num += n
    return num

luvut = [1, 2, 3, 4, 5, 6]
summa = luoLista(luvut)
print(summa)