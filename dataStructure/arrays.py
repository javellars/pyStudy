## Arrays -> matrizes
# É similar à lista (Mutable)
# Mas usamos elas quando temos uma lista muito grande
# Ou queremos aumentar a performance do código, visto que essas consomem menos memória e unidades de processamento

from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [1,2,3,4]
numeros_f = [1.5,2.5,3.5,4.5]

print(letras)
print(numeros_i)
print(numeros_f)

letras = array('u', ['a', 'b', 'c', 'd'])
# Aqui devemos sempre checkar a documentação do python para declarar o tipo da lista
# Nesse caso, o 'u' indica que temos uma lista de Strings (TypeCode)

lista1 = array('i', [1,2,3,4])

lista2 = array('f', [1.5,2.5,3.5,4.5])


print(letras)
print(lista1)
print(lista2)