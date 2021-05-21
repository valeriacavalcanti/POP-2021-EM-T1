import random

aposta = set()

while(len(aposta) < 6):
    aposta.add(random.randint(1,60))

print(aposta)
