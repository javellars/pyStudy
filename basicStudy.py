## estudos isolados de teorias básicas

##Meu nome é Jullia e tenho 21 anos, e você?
nome_anfitriao = 'Jullia'
idade = 21
idade = str(idade)

print("Meu nome é " + nome_anfitriao + " e tenho " + idade + " anos, e você?")

##aplicação de SLICE -> sempre lembrar que string é um vetor se char
print(nome_anfitriao[0:6])
print(nome_anfitriao[:: -1])

nome = input('Qual o seu nome?: ')
idade = input('Qual sua idade?: ')
idade = str(idade)

print("Meu nome é " + nome + " e tenho " + idade + " anos, prazer!")
print(nome[0:len(nome)])
print(nome[::-1])

data_nsc = input('Em que ano você nasceu?: ')
##print(type(data_nsc)) -> me dá o tipo do dado

data_nsc = int(data_nsc)
##print(type(data_nsc))

idade = 2024 - data_nsc

##aqui seria legal ter um If pra falar se fulano tem ou não a idade que falou
print("UaU! Você tem mesmo " , idade)

