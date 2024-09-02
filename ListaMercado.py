item = input('Digite o produto que deseja adicionar: ')
item.lower()
print('Digite fim quando acabar!')


lista_mercado = []

while (item != 'fim'):
    if item.lower() not in lista_mercado:
        lista_mercado.append(item)
    else:
        print('Item já registrado!')

    item = input('Digite o produto que deseja adicionar: ')
    item.lower()
