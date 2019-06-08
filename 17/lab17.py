#!/usr/bin/env python3

import math

# Laboratorio 17 - Banco de Dados Geografico
# Nome: Flavio Augusto Pereira Cunha    
# RA: 197083

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

# Funcao: Achar cidade
# 
# Parametros:
#   (int) indice da cidade a ser retornada
#
# Retorno:
#   Objeto completo da cidade com o indice dado
def findCity(i, cidades):
    for x in range(len(cidades)):
        if x == i:
            return cidades[x]
#
# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados) 
#       cep: CEP desejado 
# 
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.   
#
def consulta_cidade_por_cep(cidades, cep):
    for i in range(len(cidades)):
        if cep >= cidades[i].inicioCEP and cep <= cidades[i].fimCEP:
            return i
    return None

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio):
    # Recupera o objeto completo da cidade a partir do indice
    ref = findCity(cidadeReferencia, cidades)
    # Procura as cidades no raio e retorna suas posições
    found = [] 
    for i in range(len(cidades)):
        dist = distancia(ref.coordenadas, cidades[i].coordenadas)
        if dist < raio:
            found.append({'i': i, 'd': dist})
    # Ordena as posições com base na distância
    found.sort(key = lambda city: city['d'])
    # Retorna a lista com os indices
    indexes = [] 
    for city in found:
        indexes.append(city['i'])
    return indexes

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#          
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    # Recupera os indices das cidades no raio
    indexes = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)
    # Para cada indice no raio, soma as populaçoes de cada cidade
    s = 0
    for i in indexes:
        ref = findCity(i, cidades)
        s += ref.numHabitantes
    return s

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio):
    indexes = consulta_cidades_por_raio(cidades, cidadeReferencia, raio)
    pops = []
    # Para cada cidade no raio, salva sua população em uma lista
    for i in indexes:
        ref = findCity(i, cidades)
        pops.append(ref.numHabitantes)
    # Calcula a mediana da lista de populações
    pops.sort()
    n = len(pops)
    if n % 2 == 0:
        mid = (n-1) // 2
        median = (pops[mid] + pops[mid+1]) / 2
    else:
        mid = (n-1) // 2
        median = pops[mid]
    return median


