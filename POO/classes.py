# Classes
    # São utilizadas para criar objetos
    # objetos são partes das classes
    # utilizadas pra agrupar dados e funções

#class Funcionarios:
#    nome = 'Joao'
#    sobrenome = 'de Jesus'

#usuario1 = Funcionarios() # aqui criamos nosso primeiro objeto

#print(usuario1.nome)

# por mais que dê para adicionar os dados e criar objetos assim, a forma mais otimizada é criando funções (def)

## Criando a classe
class Funcionarios:
    pass

## Criando objetos
usuario1 = Funcionarios()
usuario2 = Funcionarios()

## Criando parâmetros do usuário1
usuario1.nome = 'Fernanda'
usuario1.sobrenome = 'Cabral'
usuario1.cargo = 'gerente'

## Criando parâmetros do usuário2
usuario1.nome = 'Carol'
usuario1.sobrenome = 'Lina'
usuario1.cargo = 'gerente'

print(usuario1.nome)
print(usuario2.sobrenome)
