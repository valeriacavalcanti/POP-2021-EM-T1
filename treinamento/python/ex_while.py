'''
Ler vários números. Parar quando o usuário digitar zero.
- quantos desses números possuem valor acima de 10
- CT: 20 10 4 20 0
'''

qtde = 0

num = int(input("Número: "))
while(num != 0):
    if (num > 10):
        qtde += 1
    num = int(input("Número: "))

print(qtde)
print(num) # SEMPRE será zero
