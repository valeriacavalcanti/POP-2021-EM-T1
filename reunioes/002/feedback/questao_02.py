pecas = 0
qtde = int(input('Quantidade: '))
tam = int(input('Tamanho: '))

tabuleiro = []
for i in range(tam):
    tabuleiro.append([0] * tam)

for i in range(qtde):
    linha, coluna = input('Posição: ').split()
    linha, coluna = int(linha), int(coluna)
    if (tabuleiro[linha][coluna] == 0):
        tabuleiro[linha][coluna] = 1
        pecas += 1

print(pecas)
