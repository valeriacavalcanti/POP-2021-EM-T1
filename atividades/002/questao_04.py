# Função 01
def index(lista, elem):
    for i in range(len(lista)):
        if (lista[i] == elem):
            return i
    return -1

# Função 02
def count(lista, elem):
    qtde = 0
    for e in lista:
        if (e == elem):
            qtde += 1
    return qtde

# Função 03
def upper(st):
    st2 = ''
    for s in st:
        if (s >= 'a' and s <= 'z'):
            st2 += chr(ord(s) - 32)
        else:
            st2 += s
    return st2

# Função 04
def isNum(st):
    for s in st:
        if (s <= '0') or (s >= '9'):
            return False
    return True

# Programa Principal

numeros = [10,20,30,20,50,20]

print(index(numeros, 20))
print(index(numeros, 100))

print(count(numeros, 20))
print(count(numeros, 100))

print(upper('valeria'))
print(upper('vAlErIa 123!!'))

print(isNum('1234'))
print(isNum('12a34'))
print(isNum('12.34'))
