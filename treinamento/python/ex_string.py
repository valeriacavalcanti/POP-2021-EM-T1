# String

frase = 'eita que BOM! 1234()*&'

print('a', ord('a'))
print('A', ord('A'))
print(97, chr(97))
print(65, chr(65))
print(97 - 32, chr(97-32))

for s in frase:
    if (s >= 'a' and s <= 'z'):
        print(s, 'é letra minúscula')
    elif (s >= 'A' and s <= 'Z'):
        print(s, 'é letra maiúscula')
    elif (s >= '0' and s <= '9'):
        print(s, 'é um número')
    else:
        print(s, 'é caractere especial')

st = 'teste'
#st[0] = 'T'
st += ' que bom!'
print(st)
