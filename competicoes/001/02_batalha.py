'''
    IFPB - CAMPUS JOÃO PESSOA
    PROJETO OLÍMPICO DE PROGRAMAÇÃO
    ENSINO MÉDIO
    TURMA: 2021 T1

    CONTEST: 001
    DATA: 11/06/2021

    QUESTÃO: 02 (BATALHA)
'''

# realiza a contagem das bombas adjacentes
def adjacencia(linha, coluna):
    qtde = 0
    # range:
    #    da linha acima (-1) até a linha abaixo (+2)
    #    da coluna a esquerda (-1) até a coluna a direita (+2)
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            # se a posição (i, j) for válida
            if (i >= 0) and (j >= 0) and (i < tamanho) and (j < tamanho):
                # se houver bomba
                if (tabuleiro[i][j] == -1):
                    qtde += 1
    return qtde

# PP

# tamanho do tabuleiro
tamanho = int(input())
# quantidade de bombas
bombas = int(input())

# montando o tabuleiro vazio
tabuleiro = []
for i in range(tamanho):
    tabuleiro.append([0] * tamanho)

# inserindo cada bomba
for i in range(bombas):
    linha, coluna = input().split()
    linha, coluna = int(linha), int(coluna)
    tabuleiro[linha][coluna] = -1

# contabilizando as bombas adjacentes
for i in range(tamanho):
    for j in range(tamanho):
        # se não tiver bomba, contabiliza
        if (tabuleiro[i][j] == 0):
            tabuleiro[i][j] = adjacencia(i, j)

# imprimindo o tabuleiro final
for linha in tabuleiro:
    st = str(linha)
    st = st.replace('-1', 'X')
    st = st.replace(',', '')
    st = st.replace('[', '')
    st = st.replace(']', '')
    print(st)
