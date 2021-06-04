def criar(tamanho):
    global matriz
    for i in range(tamanho):
        matriz.append([0] * tamanho)

def imprimir():
    for i in range(len(matriz)):
        print(matriz[i])

def add(de, para):
    matriz[de][para] = 1
    matriz[para][de] = 1

def montar():
    global matriz
    lista = [(0,1),(1,3),(3,4),(3,5),(1,2),(2,6),(2,7),(7,8),
             (7,9),(9,10),(9,11),(10,15),(10,14),(11,12),(11,13),
             (15,16),(15,17),(16,18),(16,21),(21,22),(21,23),
             (18,19),(18,20),(23,24),(23,25),(24,26),(24,27)]
    for t in lista:
        add(t[0],t[1])

def caminho(lista):
    for i in range(len(lista) - 1):
        if (matriz[lista[i]][lista[i+1]] == 0):
            return False
    return True

# programa principal

matriz = []
criar(28)
montar()
#imprimirMatriz()
print(caminho([0,1,2,7,8]))
print(caminho([0,1,2,7,9,8]))
