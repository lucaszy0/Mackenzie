#funcao 
#como funciona:
#def nome da funcao (parametros):
#instrucao 1
#instrucao 2
#...
#return valor ( opcional)

def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor  * 0.2
    return imposto


produto2 = 3500
imposto_produto1 = calcular_imposto (int(input ("digite um valor")))
imposto_produto2 = calcular_imposto(produto2)

print(imposto_produto1)