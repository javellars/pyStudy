def soma(x,y):
    adicao = int(x+y)
    print(f'A soma é {adicao}!')

def subtracao(x,y):
    menos = int(x-y)
    print(f'A subtração é {menos}!')

def multiplicacao(x,y):
    vezes = int(x*y)
    print(f'A multiplicação é {vezes}!')

def divisao(x,y):
    divide = int(x/y)
    print(f'A divisão é {divide}!')



x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
simbolo = input('Qual equação quer fazer: *, +, -, / ? ')


##como que eu melhoro isso?
if simbolo == '+':
    soma(x,y)
if simbolo == '*':
    multiplicacao(x,y)
if simbolo == '-':
    subtracao(x,y)
if simbolo == '/':
    divisao(x,y)

