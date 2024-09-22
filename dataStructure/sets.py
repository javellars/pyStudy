## Sets
# Similas às listas
# Evita itens duplicados
# Não utiliza index

lista1 = [10,20,30,40]
lista2 = [20,40,60,80]

num1 = set(lista1) # -> Transformou a lista em um conjunto de números
num2 = set(lista2)
# A partir do momento que tranformamos em um conjunto, perdemos a indexação

print(num1 | num2) # union
# o | indica a união dos dois conjuntos -> Fazendo com que os repetidos não apareçam

print(num1 - num2) # diference
# só o que tem em um e n tem no outro

print(num1 ^ num2) # symmetric diference
# retorna os valores similares nas listas, mas sem mostrar os repetidos

print(num1 & num2) # and
# tudo das duas listas

# Podemos já criar como set também, sem precisar trsnformar de Lista-> set
s1 ={9,8,7,6}

print(s1)
print(type(s1))

s1.add(5)
# não dá pra adicionar um item que já ta na lista -> se fosse 6 aqui, não mudaria nada
print(s1)

# Quando eu quero adicionar mais de um item ao sets, fica um pouco diferente
s1.update({4,3,2})
print(s1)
print(type(s1))

## Remove ou discard?
    # O remove vai remover se tiver no set, se não tiver vai dar erro
    # já o discard não vai dar erro se n tiver na lista
    # Sendo assim, o remove é útil quando você tem certeza que o que quer excluir está no conjunto
    # e o discad se mostra útil quando você não sabe ao certo de o que quer excluir está no conjunto 

s1.discard(90)
s1.add(90)

print(s1)

## SETS COM STRINGS

set1 = {'a','b','c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
set5 = set1.difference(set2)
set6 = set1.intersection(set2)
set7 = set1.symmetric_difference(set2)

print(set4)
print(set5)
print(set6)
print(set7)


# Num geral funciona da mesma forma que com Strings