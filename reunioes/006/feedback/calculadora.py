# 5 + (1 + 2) × 4 - 3

expressao = "5 1 2 + 4 × + 3 −"
pilha = []
total = 0

for termo in expressao.split():
    if (termo.isdigit()):
        pilha.append(int(termo))
    else:
        if (termo == '+'):
            num1 = pilha.pop()
            num2 = pilha.pop()

# falta concluir
