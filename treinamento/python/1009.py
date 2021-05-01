nome = input()
salario = float(input())
venda = float(input())

porcentagem = (venda * (15 / 100))

total = porcentagem + salario

print("TOTAL = R$ %.2f" % total)
