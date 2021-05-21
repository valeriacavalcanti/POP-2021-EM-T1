f=[]
while True:
  try:
    frase=input()
    ent=list(frase)
    for i in range(len(ent)):
        if ent[i]=='_':
            c1=ent.count(ent[i])
            if c1%2==0:
                del ent[i]
                ent.insert(i,'<i>')
                c1-=1
            else:
                del ent[i]
                ent.insert(i, '</i>')
                c1 -= 1

        if ent[i] == '*':
            c2 = ent.count(ent[i])
            if c2 % 2 == 0:
                del ent[i]
                ent.insert(i, '<b>')
                c2 -= 1
            else:
                del ent[i]
                ent.insert(i, '</b>')
                c2 -= 1
    f.append(ent)
  except EOFError:
    break

for y in range(len(f)):
    for z in range(0,len(f[y])):
        print(f[y][z],end='')
    print()
