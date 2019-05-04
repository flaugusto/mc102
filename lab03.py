# Este programa foi construído para calcular se o João conseguirá ou não abastecer todos os postos.
# --- Você precisará entrar com as seguintes informações:
# 1 - O valor do diâmetro do cilindro do caminhão de gasolina (metros)
# 2 - O comprimento do tanque (metros)
# 3 - A demanda de combustível do posto A }
# 4 - A demanda de combustível do posto B }(litros)
# 5 - A demanda de combustível do posto C }
# --- Saída
# A saída mostrará em cada linha se o posto foi reabastecido ou não 
# dado a quantidade disponível no tanque do caminhão.
# RA: 197083
# Nome: Flavio Augusto Pereira Cunha

d = float(input()) # diametro
h = float(input()) # comprimento
a = float(input()) # posto A
b = float(input()) # posto B
c = float(input()) # posto C

pi = 3.14
# calcula o vol do cilindro
r = d/2
m3 = pi*r*r*h # vol em m3

# converte para L
vol = m3*1000

# Se volume de der para abastecer A, abastece e tenta o próximo, 
# se não der, tenta B, em seguida C
if (vol <= a):
    print ('posto A nao foi reabastecido')
    restante = vol
else:
    print('posto A foi reabastecido')
    restante = vol - a
if (restante <= b):
    print('posto B nao foi reabastecido')
else:
    print('posto B foi reabastecido')
    restante = restante - b
if (restante <= c):
    print('posto C nao foi reabastecido')
else:
    print('posto C foi reabastecido')


