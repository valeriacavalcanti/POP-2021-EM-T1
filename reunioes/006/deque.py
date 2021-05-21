from collections import  deque

fila = []

fila.append(10)
fila.append(20)
fila.append(30)
fila.append(40)

deq = deque(fila)

print(fila)
print(deq)

while(len(fila) > 0):
    print(fila[0])
    del(fila[0])

print(deq.pop())
print(deq.popleft())
