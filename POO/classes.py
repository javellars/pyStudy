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

from datetime import datetime

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
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Lina'
usuario2.cargo = 'diretora'

print(usuario1.nome)
print(usuario2.sobrenome)

## CRIANDO CONSTRUTORES
    # Para reduzir a passagem de parâmetros

class Alunos:
    def __init__(self, nomeAluno, sobrenomeAluno, RA, ano_nsc):
        self.nomeAluno = nomeAluno # -> com o sel a gente associa o parâmetro
        self.sobrenomeAluno = sobrenomeAluno
        self.RA = RA
        self.ano_nsc = ano_nsc
    
    def nome_completo(self):
        return self.nomeAluno + ' ' + self.sobrenomeAluno
    
    def idadeFunc(self):
        ano_atual = datetime.now().year
        self.ano_nsc = int(ano_atual - self.ano_nsc)
        return self.ano_nsc
 
Aluno1 = Alunos('Joana', 'Silva', '456321', 1990)
Aluno2 = Alunos('Jéssica', 'Carolyne', '789654', 2003)

print(Aluno1.nomeAluno +' '+ Aluno1.sobrenomeAluno) # -> como reduzir isso para uma função só? A modo de replicar em vários alunos
print(Aluno1.nome_completo()) #-> Criamos a função que ja junta os parâmetros e chamamos ela (passando quem seria o Self)
print(Aluno2.nome_completo())
# -> outra forma de conseguir chamar, é referenciando a classe, e passando o self da função dessa forma
print(Alunos.nome_completo(Aluno2))
print(Alunos.idadeFunc(Aluno2))


