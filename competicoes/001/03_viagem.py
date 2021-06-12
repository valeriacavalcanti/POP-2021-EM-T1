'''
    IFPB - CAMPUS JOÃO PESSOA
    PROJETO OLÍMPICO DE PROGRAMAÇÃO
    ENSINO MÉDIO
    TURMA: 2021 T1

    CONTEST: 001
    DATA: 11/06/2021

    QUESTÃO: 03 (VIAGEM)
'''

# lista de vértices adjacentes
def adjacentes(vertice):
    lista = []
    for i in range(qt_aeroportos):
        if (matriz_voos[vertice][i] == 1):
            lista.append(i)
    return lista

# Breadth-First Search
def dfs(origem):
    pilha = []
    visitados = []
    pilha.append(origem)
    while (len(pilha) > 0):
        vertice = pilha.pop()
        visitados.append(vertice)
        for v in adjacentes(vertice):
            if (v not in visitados):
                pilha.append(v)
    return visitados


# PROGRAMA PRINCIPAL

# lista de aeroportos
aeroportos = []
# matriz de voos entre os aeroportos
matriz_voos = []

# quantidade de aeroportos
qt_aeroportos = int(input())
# leitura dos aeroportos e montagem da matriz de voos
for i in range(qt_aeroportos):
    aeroportos.append(input())
    matriz_voos.append([0] * qt_aeroportos)

# quantidade de voos
qt_voo = int(input())
for i in range(qt_voo):
    origem, destino = input().split()
    # insere o voo na matriz
    matriz_voos[aeroportos.index(origem)][aeroportos.index(destino)] = 1

# se o aeroporto destino estiver entre os aerportos alcançados a partir da origem
if (aeroportos.index(destino) in dfs(aeroportos.index(origem))):
    print('SIM')
else:
    print('NAO')
