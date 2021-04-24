# matriz

matriz = []
for i in range(2):
    matriz.append([0] * 4)

print(matriz)

matriz[0][1] = 16
print(matriz)

print(len(matriz))
print(len(matriz[0]))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = 100

print(matriz)

for i in range(len(matriz[0])):
    matriz[0][i] = 200

print(matriz)
