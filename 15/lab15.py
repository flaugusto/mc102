#!/usr/bin/env python3
# Modulo de funcões, campeonato PES
# Nome: Flavio Augusto Pereira Cunha
# RA: 197083
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
    # Quebra os itens da string de um jogo para avaliar os valores
    itens = jogo.split()
    time1 = {'nome': itens[0], 'gols': int(itens[1]), 'pontos': 0}
    time2 = {'nome': itens[4], 'gols': int(itens[3]), 'pontos': 0}
    # Verifica se o time1 ganhou do time2 ou houve empate
    if (time1['gols'] > time2['gols']):
        time1['pontos'] = 3
    elif (time1['gols'] < time2['gols']):
        time2['pontos'] = 3
    else:
        time1['pontos'] = 1
        time2['pontos'] = 1
    # Insere os pontos e os saldos de gols na tabela
    for time in tabela:
        # Procura os times que jogaram na tabela e insere os dados do jogo
        if (time[0] == time1['nome']):
            time[1] += time1['pontos'] # Soma os pontos ganhos
            # Se vitória, soma +1 vitória
            if (time1['pontos'] == 3):
                time[2] += 1
            time[3] += time1['gols'] # Saldo gols positivo
            time[3] -= time2['gols'] # Saldo gols contra
            time[4] += time1['gols'] # Soma gols pró
        if (time[0] == time2['nome']):
            time[1] += time2['pontos']
            if (time2['pontos'] == 3):
                time[2] += 1
            time[3] += time2['gols']
            time[3] -= time1['gols']
            time[4] += time2['gols']
#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
# def comparaTimes(time1, time2):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************


#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
# def ordenaTabela(tabela):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for time in tabela:
        for n in range(len(time) -1):
            print(str(time[n]) + ', ', end = '')
        print(str(time[-1]))

#*******************************************************************************