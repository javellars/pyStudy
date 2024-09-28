lista1 =[1,2,3,4,5,6]
lista2 =[6,5,4,3,2,1]

listaSoma = map(lambda x,y: x + y,lista1, lista2)
print(list(listaSoma))

listaMulti = map(lambda x,y: x*y, lista1, lista2)
print(list(listaMulti))

listaDiv = map(lambda x,y: x/y, lista1, lista2)
print(list(listaDiv))

## Agora com os inputs

valorX = input('Digite o primeiro valor: ')
valorY = input('Digite o segundo valor: ')
sinal = input('Escolha * para multiplicação, / para divisão, + para soma e - para subtração: ')

# tranformando assim conseguimos contornar o problema da concatenação na soma
valorX = list(map(int, valorX))
valorY = list(map(int, valorY))

if sinal == '+':
    listaSoma = map(lambda x,y: x + y,valorX, valorY)
    print(list(listaSoma))
if sinal == '-':
    listaSub = map(lambda x,y: x - y,valorX, valorY)
    print(list(listaSub))
if sinal == '*':
    listaMulti = map(lambda x,y: x * y,valorX, valorY)
    print(list(listaMulti))
if sinal == '/':
    listaDiv = map(lambda x,y: x / y,valorX, valorY)
    print(list(listaDiv))

