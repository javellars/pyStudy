lista1 =[1,2,3,4,5,6]
lista2 =[6,5,4,3,2,1]

listaSoma = map(lambda x,y: x + y,lista1, lista2)
print(list(listaSoma))

listaMulti = map(lambda x,y: x*y, lista1, lista2)
print(list(listaMulti))

listaDiv = map(lambda x,y: x/y, lista1, lista2)
print(list(listaDiv))

      