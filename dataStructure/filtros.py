# Filter Function
    # A estrutura de como utilizar o filter é similar ao Map (no entanto, eles não são a mesmas coisas)
    # Muito utilizado com listas
    # Aplica uma função à um iterable, filtrando o items. (list, tuple, dicionary etc.)

valores = [10,20,30,40,50,60]

def remove20(x): 
    return x > 20

# dessa forma ele retorna pra gente de forma booleana x > 20
print(list(map(remove20, valores)))

# assim conseguimos filtrar x > 20 e exibir só eles
print(list(filter(remove20, valores)))

# A gente pode simplificar tudo isso aplicando lambda
print(list(filter(lambda x: x > 20,valores)))

# map -> associa uma função a uma lista
# flter -> assosia uma função a uma lista, mas retira o resultado daquela função