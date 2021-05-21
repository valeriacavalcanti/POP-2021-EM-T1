freq = {}
st = input("Frase: ")

for s in st:
    if (not s in freq.keys()):
        freq[s] = 1
    else:
        freq[s] += 1

print(freq)
