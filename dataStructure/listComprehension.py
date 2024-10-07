# List comprehension
    # mais simples de escrever
    # Utilizada quando você precisa criar uma nova lista a partir de uma existente
    # [expressão for item in item]

frutas1 = ['abacate', 'banana', 'morango','uva']
frutas2 =[]

# dessa forma podemos colocar todas as frutas que aparecem B na lista 'frutas2'
for item in frutas1:
    if 'b' in item:
        frutas2.append(item)
print(frutas2)

# no entanto, tem uma maneira mais simples de conseguir fazer isso 
frutas3 = [iten for iten in frutas1 if 'n' in iten]

print(frutas3)

## Agora podemos fazer a manipulação com números

valores = [x * 10 for x in range(6)]

print(valores)