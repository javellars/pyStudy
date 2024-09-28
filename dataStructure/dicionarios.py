## Dicionários -> utiliza index no formato key: values
#           key   value
alunos = {'nome': 'Ana', 'idade': 16, 'notaFinal': 'A', 'aprovação': True}

print(alunos)
print(alunos['nome']) # index no formato de Key

# Para add no dicionario fazemos da seguinte forma:

alunos['alunos'] = 'josé' # Assim conseguimos adicionar um por vez
print(alunos)

alunos.update({'nome': 'maria', 'idade': '25', 'notaFinal': 'C', 'aprovação': False} ) # assim conseguimos add várias keys e values 
print(alunos)

alunos.update({"endereço": 'Rua A'}) # add uma nova key
print(alunos)

# Quando procuramos ou solicitamos uma key que não existe, recebemos um erro
# no entanto, podemos contornar para que ele retorne a indicação de que não existe, ao invés do erro

print(alunos.get('familia', 'O valor não existe'))

del alunos['idade'] # deletando uma key
print(alunos)