# Este programa foi construído para auxiliar a Aliança Rebelde a melhorar a eficiência de suas
# espaçonaves. Ele serve para dizer se existe um balanceamento perfeito dos quatro containeres
# de suprimentos fornecidos ao programa para o calculo.
# # --- Para usar o programa, você precisará entrar com as seguintes informações:
# 1 - O peso do container 1
# 2 - O peso do container 2
# 3 - O peso do container 3
# 4 - O peso do container 4
# --- Saída
# A saída mostrará em uma linha com "sim" se for possível o balanceamento, ou "não" se não.
# RA: 197083
# Nome: Flavio Augusto Pereira Cunha

import sys
c1 = int(input()) #container 1
c2 = int(input()) #container 2
c3 = int(input()) #container 3
c4 = int(input()) #container 4


# a função testa se os lados estão equilibrados
# se for possível, o programa não precisa testar mais e sai, senão, continua os testes
def test(a,b):
    if (a == b):
        print('sim')
        sys.exit()
    else:
        return False

total = c1 + c2 + c3 + c4
# se a soma total for impar, não se pode definir uma divisão em duas partes iguais
if (total % 2 != 0):
    print('nao')
else:
    # faz as combinações entre os pesos 2 a 2 
    # se é possível obter uma divisão igual
    # nos dois lados da nave
    a = c1 + c2
    b = c3 + c4
    r = test(a,b)
    a = c2 + c3
    b = c1 + c4
    r = test(a,b)
    a = c1 + c3
    b = c2 + c4
    r = test(a,b)
    # se nenhuma dessas for possível, testa de 1 a 3
    a = c1
    b = c2 + c3 + c4
    r = test(a,b)
    a = c2
    b = c1 + c3 + c4
    r = test(a,b)
    a = c3
    b = c1 + c2 + c4
    r = test(a,b)
    a = c4
    b = c1 + c2 + c3
    r = test(a,b)
    # se não encontrar nenhuma combinação dividindo os lados igualmente, sai com 'não'
    if (r == False):
        print('nao')