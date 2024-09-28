# Lambda function
    # É uma função pequena sem nome -> ela sempre chama lambda
    # pode ter argumentos de mais de uma função 
    # muito utilizad dentro de outras funções
    # Código mais "clean"
    # lambada -> argumento -> função
    # é uma """subfunção""", usamos mais quando precisamos fazer uma função com alguma ougra função

somar = lambda x,y: x+y
print(somar(3,4))

## Lambda dentro de uma outra função -> pra evitar de escrever duas funções

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))