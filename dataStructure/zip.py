## O que a gente faz aqui não é uma concatenação, e sim uma junção de duas listas
## Sendo assim, nós temos uma tuple, uma "mini lista" c as infos das duas listas
## Resultando em pequenas listas de duas listas (ou mais)

cores = ['amarelo', 'verde', 'azul', 'vermelho']

valores = [10,20,30,40]


var = list('Comprar')
print(var)

duas_listas = zip(cores,valores)
print(duas_listas)
print(list(duas_listas))