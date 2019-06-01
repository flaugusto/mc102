#!/usr/bin/env python3
# Biblioteca de funções, teoria dos conjuntos
# Nome: Flavio Augusto Pereira Cunha
# RA: 197083


# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    if num in conj:
        return True
    else:
        return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    for x in conj1:
        if not pertence(conj2, x):
            return False
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    if not pertence(conj, num):
        conj.append(num)
    return

def subtracao(conj, num):
    if pertence(conj, num):
        conj.remove(num)
    return

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    # Testa primeiro se conj1 não está contido em conj2, pois se verdadeiro, a união é conj2
    if contido(conj1, conj2):
        return conj2
    u = []
    # Acha os elementos do conj1 que não estão no conj2 e insere
    for x in conj1:
        if not pertence(conj2, x):
            u.append(x)
    # Depois adiciona o conj2
    u += conj2
    return u

def intersecao(conj1, conj2):
    n = []
    # Testa primeiro se não há continência
    if contido(conj1, conj2):
        return conj1
    # # Acha os elementos do conj1 que estão no conj2 e insere
    for x in conj1:
        if pertence(conj2, x):
            n.append(x)
    return n

def diferenca(conj1, conj2):
    # Primeiro pega a intersecção de conj1 em conj2
    i = intersecao(conj1, conj2)
    # Depois retorna os elementos de conj1 que não pertecem a intersecção
    d = []
    for x in conj1:
        if not pertence(i, x):
            d.append(x)
    return d

def uniao_disjunta(conj1, conj2):
    # Primeiro, faz as diferenças conj1 \ conj2 e conj2 \ conj1
    d1 = diferenca(conj1, conj2)
    d2 = diferenca(conj2, conj1)
    # Depois retorna o conjunto união das diferenças
    return uniao(d1, d2)
