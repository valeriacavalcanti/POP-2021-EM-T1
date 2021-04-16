media1 = 60
media2 = 80

print(media1 >= 70)
print(media2 >= 70)

if (media1 >= 70):
    print('Aprovado')
else:
    print('Reprovado')

if (media2 >= 70):
    print('Aprovado')
else:
    print('Reprovado')

if (True):
    print('Eita')
else:
    print('que coisa')


'''
Loja
[0..100] - 2 vezes
]100 .. 200] - 4 vezes
]200 ... ?] - 6 vezes
'''
v1 = 100
v2 = 200
v3 = 250
v4 = 300

if (v3 <= 100):
    print('2 vezes')
else:
    #certeza! acima de 100
    if (v3 <= 200):
        print('4 vezes')
    else:
        # certeza! acima de 200
        print('6 vezes')

if (v1 <= 100):
    print('2 vezes')
elif (v1 <= 200):
    print('4 vezes')
else:
    print('6 vezes')
