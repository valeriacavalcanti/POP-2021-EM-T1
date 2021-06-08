def criar(tamanho):
    global lista_adjacencias
    for i in range(tamanho):
        lista_adjacencias.append([])

def imprimir():
    for i in range(len(lista_adjacencias)):
        print(lista_adjacencias[i])

def add(de, para):
    lista_adjacencias[de].append(para)
    lista_adjacencias[para].append(de)

def montar():
    lista = [(0,1),(1,3),(3,4),(3,5),(1,2),(2,6),(2,7),(7,8),
             (7,9),(9,10),(9,11),(10,15),(10,14),(11,12),(11,13),
             (15,16),(15,17),(16,18),(16,21),(21,22),(21,23),
             (18,19),(18,20),(23,24),(23,25),(24,26),(24,27)]
    for t in lista:
        add(t[0],t[1])

def caminho(lista):
    for i in range(len(lista) - 1):
        if (lista[i + 1] not in lista_adjacencias[lista[i]]):
            return False
    return True

def vizinhos(vertice):
    pass

def dfs(origem):
    pilha = []
    marcados = []
    pilha.append(origem)
    while(len(pilha) > 0):
        vertice = pilha.pop()
        marcados.append(vertice)
        for v in vizinhos(vertice):
            if (v not in marcados):
                pilha.append(v)
    return marcados

def bfs(origem):
    fila = []
    marcados = []
    fila.append(origem)
    while (len(fila) > 0):
        vertice = fila[0]
        del(fila[0])
        marcados.append(vertice)
        for v in vizinhos(vertice):
            if (v not in marcados):
                fila.append(v)
    return marcados


# programa principal

lista_adjacencias = []
criar(28)
montar()
#imprimirMatriz()
print(caminho([0,1,2,7,8]))
print(caminho([0,1,2,7,9,8]))
