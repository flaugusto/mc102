# Este programa foi criado para interceptar as postagens feitas na rede social
# FACESTAR e descobrir através do nosso informante infiltrado quais direções e elevações
# dos nossos canhões devemos utilizar para atacarmos as bases da império antes que nos ataquem.
# Entrada: Um texto de no máximo 1000 caracteres sendo a postagem no FACESTAR.
# Saída: As direções e elevações de cada basa identificada no texto, uma em cada linha.

# Nome: Flavio Augusto Pereira Cunha
# RA: 197083

# post = input()
post = 'GoRIla fUNeBREs ROTuLagem nEtUNo OraTorio vErmeLHo esquIva eMbATe traJetoriA EXTRaVIo uRANO cLIticO VERmeLhO ESPOrTIVO cRoCantE saBotAgem merCUriO pApEL vEntOSIdade INtEMPeSTiVo INStituCIonalIZaCao VErDe poLiPO conflITo ALVorocaMEnTo nEtUno desseRvICO fausTo EmBoneCADo AmARelO dIgNo PARTO NAvajO emPoLGAcAo imPerMeabiLIDaDE URanO ReconfORtaNtE TELUGu peNeirA AGlOMERaCao imPoSSiBILIdaDe veRde chiaDeIRa trIANGuLAr FANTasistA sAturNO diFIcIl Plangente nOCiVidade HORTO cRACk vErmelhO bASbaqUiCe EnroLADOr reElegEr ClINicAR CafEiCuLTOR teRrA coMovEr PoSsEs boTAo APAssivAr BLAsFEmaR VeRdE BuROCRATiZaCaO esTERcAr AFOBAdo AlUMINiFerO'
post = post.lower()


# Dicionário para os pares de valoes direção / elevação
pairsFound = {}

# Função que procura as palavras chave de direções no texto e retorna suas posições na ordem em que foram encontradas
def findDirections(text):
    # Dicionário palavras-chave > direções
    directions = {
        'mercurio': 'N',
        'venus': 'NE',
        'terra': 'L',
        'marte': 'SE',
        'jupiter': 'S',
        'saturno': 'SO',
        'urano': 'O',
        'netuno': 'NO'
    }
    positions = []
    # Para cada direção:
    for key, direction in directions.items():
        start = 0
        # Procura todas as ocorrências até que não tenha mais nenhuma
        while text.find(key, start) != -1:
            pos = text.find(key, start)
            item = {
                'direction': direction,
                'position': pos
            }
            # E salva a posição encontrada junto com a direção correspondente
            positions.append(item)
            start = pos + 1
    # Ordena a lista de direções de acordo com a ordem que apareceram no texto
    positions.sort(key= lambda pair: pair['position'])
    return positions

# Função que procura as palavras-chave de elevações a partir de uma posição no texto (no caso após a direção)
def findElevations(pos):
    # Dicionário palavras-chave > ângulos de elevação
    elevations = {
        'verde': '30',
        'amarelo': '45',
        'vermelho': '60'
    }

    minorElevation = {'strPos': len(post), 'elevation': 0 }
    for eleKey, elevation in elevations.items():
        elePos = post.find(eleKey, dirPos)
        if (elePos != -1):
            if (elePos < minorElevation['strPos']):
                minorElevation['strPos'] = elePos
                minorElevation['elevation'] = elevation

# pairsFound[direction] = minorElevation['elevation']

# print(pairsFound)
