alunos = {'nome': 'Ana',
            'idade': 16,
            'notaFinal': 'A', 
            'aprovação': True, 
            'materias': ['Fisica', 'Matematica', 'ingles']
        }

print(alunos)

print(alunos.get('materias'))

# pra saber a quantidade de keys
print(len(alunos))

# imprime as keys
print(alunos.keys()) # -> dicionario de keys

# imprimir os valores e keys
print(alunos.items()) # -> dicionario de itens 

# imprime so os valores
print(alunos.values()) # -> dicionatio de valores