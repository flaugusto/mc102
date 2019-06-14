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
# Dicionário palavras-chave > ângulos de elevação
elevations = {
    'verde': '30',
    'amarelo': '45',
    'vermelho': '60'
}
# Dicionário para os pares de valoes direção / elevação
pairsFound = {}

# Varre a string do post procurando direções e se encontrar alguma, procura por elevações
for dirKey, direction in directions.items():
    dirPos = post.find(dirKey)
    # Se a direção for encontrada, procura elevações no texto após ela
    if (dirPos != -1):
        minorElevation = {'strPos': len(post), 'elevation': 0 }
        for eleKey, elevation in elevations.items():
            elePos = post.find(eleKey, dirPos)
            if (elePos != -1):
                if (elePos < minorElevation['strPos']):
                    minorElevation['strPos'] = elePos
                    minorElevation['elevation'] = elevation

        pairsFound[direction] = minorElevation['elevation']

print(pairsFound)


