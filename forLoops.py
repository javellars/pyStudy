## aplicando para strings
palavra = input('Digite uma palavra: ')

##qnt_letras = 0

for letra in palavra:
    print(letra)
    ##qnt_letras += palavra.count(letra)

print(f'A palavra tem {len(palavra)} letras!')

## utilizando if e else

compra_confirmada = True
dados_compra = 'Compra no valor de 12,50'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('A compra foi efetuada com sucesso! Recibo enviado para seu email')
        break
    else:
        print('falha na compra')

## nested loops -> o inner loop gira dentro do outer loop
    ##outer loop
        ##inner loop

for numero_titulo in range(1,6):
    print('numero título:' + str(numero_titulo))
    for numero_caracteristica in range(5):
        print(numero_caracteristica)



## for loops aplicando em Strings

palavra2 = input('Digite uma palavra: ')

for espaco in palavra2:
    print(f' {espaco}', end='')
    print( )

## Criação de um retângulo 6x6 usando for loops

linhas = 6
colunas = 6
simbolo = '*'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end= '')
    print( )


## while loops -> ótimos pra quando o loop depende de uma condição

valor = 100
dia = 1

while valor > 20:
    dia += 1
    print(f'O dia é {dia} e o valor do produto hoje é {valor}')
    valor -= 5 

## operador ternário