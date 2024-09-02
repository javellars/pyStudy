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

