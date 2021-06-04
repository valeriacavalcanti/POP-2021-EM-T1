def criar(quantidade):
    global matriz
    for i in range(quantidade):
        matriz.append([0] * quantidade)

def addVertice(de, para):
    matriz[de][para] = 1
    matriz[para][de] = 1

def imprimir():
    for linha in matriz:
        print(linha)

# Programa Principal
matriz = []

qtde = int(input("Quantidade de vértices: "))
criar(qtde)

addVertice(0,1)
addVertice(0,2)
addVertice(0,3)
addVertice(0,4)
addVertice(2,3)
addVertice(2,4)

imprimir()

