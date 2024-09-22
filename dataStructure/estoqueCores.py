cores = ['amarelo', 'verde', 'azul', 'vermelho']

corDesejada = input("Digite a cor desejada:")
corDesejada = corDesejada.lower() ## pra conseguirmos achar de qualquer forma que a cor for digitada

if corDesejada in [i.lower() for i in cores] :
    print(f'{corDesejada} em estoque!')
else: 
    print("Não temos essa cor em estoque!")