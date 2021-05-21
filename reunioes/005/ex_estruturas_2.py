lista = [1,2,3,4]
tupla = (1,2,3,4)
pessoa = {}
dicionario2 = dict()
pessoas = []

print(type(lista), lista)
print(type(tupla), tupla)

pessoa["nome"] = "valéria"
pessoa["idade"] = 15
pessoa["email"] = "valeria.cavalcanti@"
pessoa["fone"] = "1234.1234"
pessoa["nome"] = "valéria maria"
pessoa["idade"] += 1

pessoas.append(pessoa)

print(pessoa)
print(pessoa["nome"])

print(pessoa.keys())
print(pessoa.items())
print(pessoa.values())
