numeros = []
while (len(numeros) < 10):
    num = int(input())
    if (num not in numeros):
        numeros.append(num)

print(numeros)
