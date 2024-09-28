# Map function
    # muito utilizada com listas
    # aplicar uma função a un iterável, por item. (List, tuple, dic etc.)

lista1 = [1,2,3,4]

def multi(x):
    return x*2


lista2 = map(multi, lista1)

# dessa forma ele vai printar o elemnto da lista
print(lista2)
# sendo assim, precisamos converter dnv para uma lista
print(list(lista2))

# Em resumo no map a gente consegue fazer com que uma função seja aplicada a itens dentro de uma lista e a gente tenha o resultado

# dessa forma a gente consegue resumir as 4 linhas de cima nisso aqui
lista3 = map(lambda x: x*2, lista1)

print(list(lista3))

# Conseguimos também unir lambda com o map pra ter um resultado similar
print(list(map(lambda x: x * 2, lista1)))
# dessa forma conseguimos criar uma função e mapear ela a uma lista, e a partir disso tranformamos em lista e printamos na tela