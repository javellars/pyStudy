##conceitos básicos - estudo do oráculo 1

lista = [5,2,3,1,4,6]

## ToDo: procure o menor elemento com um laço for
menor = lista[0]

for el in lista:
  if el < menor:
    menor = el
print("o menor com for é:", menor)


## ToDo: procure o menor elemento com um laço while
menor = lista[0]

i = 1

while i < len(lista):
  if i < menor:
    menor = i
  i += 1
print("o menor com While é:", menor)