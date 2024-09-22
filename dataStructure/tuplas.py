## Tuplas
# armazenam mais de uma info em variáveis
# Mantém uma sequência dos dados em uma variável
# Não podem ser alteradas (immutable) -> é a diferença para as Listas(mutable)

cores = ('amarelo', 'azul', 'verde') # -> aqui usamos parênteses!!!

print(cores)
print(type(cores))

# A gente não consegue adicionar itens, como fazemos nas listas -> immutable
## Quando ent criar uma tuple, ao invés de uma lista?
    # Listas gastam um espaço maior de memória, sendo assim, quando não temos intenção de que o usuário modifique algo
    # devemos optar por usar tuples