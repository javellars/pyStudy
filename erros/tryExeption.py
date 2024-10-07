# Erros
    # Excelente para testes
    # não para o programa
    # podemos customizar mensagens quando encontramos algum erro

try:
    letras =['a','b','c','d','e']
    print(letras[6])
except IndexError:
    print('index não existe')

## Implementando try e Excep com input

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(f'O valor digitado foi {valor}!')
except ValueError:
    print('Digite um valor em números inteiros')

## Adicionando Else e finally


try:
    valor = int(input('Digite o valor do seu produto: '))
    print(f'O valor digitado foi {valor}!')
except ValueError:
    print('Digite um valor em números inteiros')
else:
    resultado = 2 * valor
    print(resultado)

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(f'O valor digitado foi {valor}!')
except ValueError:
    print('Digite um valor em números inteiros')
finally:
    print('segue o baile!')

# Se a gente quer retornar algo se a tentativa for positiva aplicamos o else
# Se a gente precisar acessar/mostrar/solicitar algo, independente de ter dado erro ou não, colocamos finally