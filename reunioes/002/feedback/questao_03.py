nome = input('Nome: ')
iniciais = ''

nome = nome.upper()
nome = nome.split()
for i in range(len(nome)):
    iniciais += str(ord(nome[i][0]))

print(iniciais)
