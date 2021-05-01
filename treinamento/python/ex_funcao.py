def minha_count(lista, item):
    qtde = 0
    for i in range(len(lista)):
        if (lista[i] ==  item):
            qtde += 1
    return qtde

def minha_find(lista, item):
    for i in range(len(lista)):
        if (lista[i] == item):
            return i
    return -1

# programa principal

numeros = [1,3,5,7,9,10,5,2,5,5]

quantidade = minha_count(numeros, 5)
print(quantidade)
print(minha_count(numeros, 10))

print(minha_find(numeros, 5))
print(minha_find(numeros, -5))
