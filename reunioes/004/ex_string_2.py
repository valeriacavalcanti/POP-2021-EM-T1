nome = 'cauani'

# contar
print(nome.count('a'))
print(nome.count('i'))
print(nome.count('v'))

qtde = 0
for i in range(len(nome)):
    if (nome[i] == 'a'):
        qtde += 1

print(qtde)

# verificar se existe
print(nome.find('a'))
print(nome.find('i'))
print(nome.find('v'))

posicao = -1
for i in range(len(nome)):
    if (nome[i] == 'v'):
        posicao = i
        break

print(posicao)
