def criar(quantidade):
    global matriz
    for i in range(quantidade):
        lista.append([])

def addVertice(de, para):
    lista[de].append(para)
    lista[para].append(de)

def imprimir():
    for i in range(len(lista)):
        print(i, lista[i])

# Programa Principal
lista = []

qtde = int(input("Quantidade de vértices: "))
criar(qtde)

addVertice(0,1)
addVertice(0,2)
addVertice(0,3)
addVertice(0,4)
addVertice(2,3)
addVertice(2,4)

imprimir()
