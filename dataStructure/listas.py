## listas

#               -4              -3              -2          -1
cidades = ['Rio de janeiro', 'São Paulo', 'Minas gerais', 'Goiânia']
#               1               2               3              4

print(cidades)

# print(cidades[2]) -> podemos indexar assim pra pedir pra exibir determinado item

cidades[2] = 'Brasília' # -> dessa forma nós trocamos o dado no determinado index

cidades.append('Santa Catarina') # -> adiciona no final da lista

cidades.remove('Goiânia') # -> remove o item

cidades.insert(1, 'Limeira') # -> adiciona o dado no index indicado

cidades.pop(0) # -> retira a posição indicada

cidades.sort() # -> ordena em ordem alfabética

print(cidades)


numeros = [1,2,3,4,5]
letras = ['a', 'b', 'c', 'd']

## Dessa forma nós concatenamos as listas
# final = numeros + letras
# print(final)

## Dessa forma também!!!
numeros.extend(letras)
print(numeros)
