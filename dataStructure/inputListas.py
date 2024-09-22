# Criar uma lista de roupas inseridas pelo usuário

roupasUsuario = input("Digite suas roupas preferidas, separadas por vírgula: ")

listaRoupas = roupasUsuario.split(', ') # -> esse Split lembra o conceito de Split em árvore B

print(listaRoupas)