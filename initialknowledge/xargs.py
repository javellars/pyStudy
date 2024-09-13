## Xarg -> vários argumentos (o * antes do numeros significa que não sabemos a qnt de valores ainda)

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado +=num
    return resultado

## aqui ele adere ao x o resultado da função soma, e insere os valores que ele quer
x = soma(1,2,3,4)
print(x) 

## Agora criando uma função que armazena numeros e String (dados), identificando o parâmetro

## adicionando os ** eu indico que ao invés de receber vários argumentos, vou receber vários parâmetros 
def agencia(**carro):
    return carro ##-> aqui eu usei o return e depois o print para registrar meus dados e exibi-los, ao inves de so exibi-los

print(agencia(marca = 'BYD', cor = 'azul', modelo = 'elétrico'))
print(agencia(marca = 'Toyota', cor = 'prata', modelo = 'conversível', placa = 'xxr8'))