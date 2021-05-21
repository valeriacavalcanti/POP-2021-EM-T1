lances = {}

for i in range(5):
    nome = input()
    valor = float(input())
    if (valor not in lances.keys()):
        lances[valor] = [nome]
    else:
        lances[valor].append(nome)

print(lances)
print(lances.keys())
print(lances.values())
print(lances.items())
