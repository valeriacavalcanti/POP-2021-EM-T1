'''
    IFPB - CAMPUS JOÃO PESSOA
    PROJETO OLÍMPICO DE PROGRAMAÇÃO
    ENSINO MÉDIO
    TURMA: 2021 T1

    CONTEST: 001
    DATA: 11/06/2021

    QUESTÃO: 04 (TURISMO)
'''

# dicionário com as cidades
cidades = {}

# Leitura da pesquisa
for i in range(1000):
    cidade = input()
    # se a cidade já foi registrada
    if (cidade in cidades.keys()):
        # contabiliza
        cidades[cidade] += 1
    else:
        # insere o primeiro registro
        cidades[cidade] = 1

# maior valor encontrado na contabilidade dos votos
maior = max(cidades.values())

print(maior, end=' ')

# exibindo a(s) cidade(s) que possui(em) a maior contabilidade
for cidade, qtde in cidades.items():
    if (qtde == maior):
        print(cidade, end=' ')
