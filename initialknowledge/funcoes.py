## default -> parâmetro n alteravel (dá pra sobreescrever)
## non-default -> parametro alteravel
## non-default sempre vem primeiro q o default!

##Print vs return

def nome1(nome):
    print(f'{nome}')

## Se eu só pedir pra ele exibir o valor da função ele dá o nome que eu inseri
## No entanto, se eu peço para ele printar o retorno dessa função, ele me dá none
## Isso acontece porque o print apenas exibe o dado que determinamos
print(nome1('carlos'))


def nome2(nome):
    return f'{nome}'

## nesse caso, como eu dei return ao invés de print, ele vaiarmazenar o determinado dado
## sendo assim, caso eu apenes chame a função, nada será exibido
## Caso eu queira exibir o determinado dado armazenado, printar o registro da função é necessário
print(nome2('Maricota'))

