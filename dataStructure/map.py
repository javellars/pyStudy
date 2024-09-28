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