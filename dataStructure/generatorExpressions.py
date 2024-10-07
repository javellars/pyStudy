# Generator Expressions 
    # Uma forma mais rápida de gerar listas, dicionários e afins
    # menos memória alocada
    # valores em bytes

from sys import getsizeof

numeros =[ x * 10 for x in range(100)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print(f'Agora um generator expression')

numeros =( x * 10 for x in range(100)) # -> quando a gente troca [] por () tranformamos em generator Expression
print(type(numeros))
print(numeros) # -> se quiser transformar em lista é so converter para list
print(getsizeof(numeros))
