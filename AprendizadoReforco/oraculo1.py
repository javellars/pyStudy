##conceitos básicos - estudo do oráculo 1

lista = [5,2,3,1,4,6]

## ToDo: procure o menor elemento com um laço for
menor = lista[0]

for el in lista:
  if el < menor:
    menor = el
print("o menor com for é:", menor)


## ToDo: procure o menor elemento com um laço while
menor = lista[0]

i = 1

while i < len(lista):
  if i < menor:
    menor = i
  i += 1
print("o menor com While é:", menor)
##quando passamos o valor de uma variável utilizamos separaçãopor ','


##funções

def ola():
  print("Olá mundo, via função!")

ola()
##a chamada na função lembra a chamada de funções em C, não temos ';' assim como Kotlin

##função com frase pré determinada, porém com variável
def ola_user(user):
  print("Olá, seja bem vinde %s" %user)
  ##quando usamos a chamada de um ""tipo"" não colocamos a separação por ','
ola_user("marcinho")

##exemplo de atribuição por valor padrão -> primeiro definimos uma variável como necessária, mas podemos "reescrevê-la" passando um novo valor
def ola_mundo( user = "mundo"):
  print("Olá %s" %user)

ola_mundo()
ola_mundo("fernanda")

## plots a partir de funções -> o que aconteceu aqui?

##import pandas as pd # type: ignore

##faithful = pd.read_csv("https://raw.githubusercontent.com/ulissesdias/tt003/main/dados/atv2024_01.csv", index_col = 0)
##faithful.head()
