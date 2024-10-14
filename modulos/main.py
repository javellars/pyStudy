import funcoes # -> a gente pode importar assim (e trazer todas as funções)
from funcoes import somar # -> ou podemos importar assim, e trazer apenas a função especificada aqui
from funcoes import somar,subtrair # -> dá pra fazer dessa forma também
from items.cadastros import cliente # -> ai podemos ir add as funções aqui

# ->dessa maneira conseguimos chamar as funções que temos no outro módulo
funcoes.somar()
funcoes.subtrair()

somar()
subtrair()

cliente()

## Sendo assim, o que podemos resumir da "hierarquia" é que:
    # várias funções -> um módulo
    # vários módulos -> um package