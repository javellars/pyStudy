## estudos isolados de teorias básicas

##Meu nome é Jullia e tenho 21 anos, e você?
nome_anfitriao = 'Jullia'
idade_anfitriao = 21
idade_anfitriao = str(idade_anfitriao) ##conversão de tipo

print("Meu nome é " + nome_anfitriao + " e tenho " + idade_anfitriao + " anos, e você?")

##aplicação de SLICE -> sempre lembrar que string é um vetor se char
print(nome_anfitriao[0:6])
print(nome_anfitriao[:: -1])

nome_convidado = input('Qual o seu nome?: ')
idade_convidado = input('Qual sua idade?: ')
idade_convidado = str(idade_convidado)

print("Meu nome é " + nome_convidado + " e tenho " + idade_convidado + " anos, prazer!")
print(nome_convidado[0:len(nome_convidado)])
print(nome_convidado[::-1])

data_nsc = input('Em que ano você nasceu?: ')
##print(type(data_nsc)) -> me dá o tipo do dado

data_nsc = int(data_nsc)
##print(type(data_nsc))

teste_idade = 2024 - data_nsc
teste_idade = str(teste_idade)

if  teste_idade == idade_convidado :
    print("UaU! Você tem mesmo " , idade_convidado)
else:
    print("Você mentiu a idade")


if idade_anfitriao == idade_convidado:
    print('tem a mesma idade!')
elif idade_anfitriao < idade_convidado:
    print(nome_convidado + ' é mais velho que ' + nome_anfitriao)
else:
    print( nome_anfitriao + ' é mais velho que ' + nome_convidado)


##String formatada
texto1 = f"Agora {nome_anfitriao} e {nome_convidado} já se conhecem!"

print (texto1)
##colocar um condicional pra falar se tem a mesma idade




##métodos para String
##print(mensagem.upper()) -> imprime todo o texto da mensagem em maiúsculo
##print(mensagem.lower()) -> imprime todo o texto da mensagem em minusculo
##print(mensagem.captalize()) -> põe a primeira em maiúsculo
##print(mensagem.find('a')) -> vai procurar o caractere informado e informar a posição dele
##print(mensagem.find('palavra')) -> me dá a posição que determinada palavra inicia [-1 significa que não achou]
##print(mensagem.replace('a', 'e')) -> substitui todo a por e; podemos utilizar com palavras também
##print(mensagem.strip()) -> remove os espaços que tem antes do primeiro caractere

