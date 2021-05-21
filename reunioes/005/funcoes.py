def distintos(lista):
    return (len(set(lista)) == len(lista))

def media(lista):
    return sum(lista)/len(lista)

def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def prints(st, n):
    #for s in st:
    for i in range(len(st) - 1):
        print(st[i], end=" " * n)
    print(st[len(st) - 1])

def ordenado(lista):
    for i in range(len(lista) - 1):
        if (lista[i] > lista[i + 1]):
            return False
    return True

# programa principal

print(distintos([1,2,3,4]))
print(distintos([1,2,3,4,2]))
print(media([1,2,3,4,5,6,7,8,9,10]))
print(maior([1,2,3,4]))
print(menor([1,2,3,4]))
prints("IFPB", 4)
print(ordenado([1,2,3,4]))
print(ordenado([10,2,3,4]))
