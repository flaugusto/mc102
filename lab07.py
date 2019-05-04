# Este programa simula uma luta do jogo Street Fighter
# Assumindo que existem 2 lutadores (Ryu e Ken), cada um com 50 pontos de vida
# o programa calculará com base em alguns dados e critérios quem ganhou a luta.
# ----
# O programa espera como entrada uma sequência de números inteiros, tal que
#     se positivos é um golpe do Ryu
#     se negativos é um golpe do Ken
# Ao final das entradas os golpes são computados e calcula-se se alguém venceu 2 rounds,
# caso cada lutador ganhe 1 round será considerado empate.
# ----
# A saída será uma sequência de mensagens represantando o andamento da luta.
# Por fim a última saída é o resultado de quem venceu, ou se houve um empate.


# variaveis auxiliares ao programa (não são entradas)
hp = 50
ryu = hp 
ken = hp
lastRyuPv = hp
lastKenPv = hp
roundCounter = 0
ryuDmg = 0
kenDmg = 0
lastRyuHit = 0
lastKenHit = 0
ryuWins = 0
kenWins = 0 
hitsCounter = 0
    
# Função módulo
def absolute(x):
    if (x >= 0):
        return x
    else: 
        return -x

while (roundCounter <= 2):
    hit = int(input()) # entrada de cada golpe
    
    # Identifica de quem é o golpe da entrada
    if( hit < 0):
        negative = True
        if (ryu > 0):
            ryu += hit
            ryuDmg -= hit
            lastRyuHit = 0
        else:
            lastRyuHit = hit
    else:
        negative = False
        ken -= hit
        kenDmg += hit
    
    if (ryu <= 0 or ken <= 0):
        if(ryu <= 0):
            ryuWins += 1
        if(ken <=0):
            kenWins += 1
        roundCounter +=1
        ryu = hp
        ken = hp
        lastKenPv = hp
        lastRyuPv = hp
    
    # Este bloco criará as sequências de golpes se o hit for do mesmo lutador
    if (hitsCounter == 0):
        prevNum = negative
    else:
        #Quando o sinal da entrada mudar, termina a sequencia e exibe os valores
        if (prevNum != negative):
            print('Ken: ' + str(lastKenPv) + ' - ' + str(kenDmg) + ' = ' + str(ken))
            print('Ryu: ' + str(lastRyuPv) + ' - ' + str(ryuDmg) + ' = ' + str(ryu))
            lastRyuPv = ryu
            ryuDmg = 0
            lastKenPv = ken
            kenDmg = 0
            hitsCounter = 0
            prevNum = negative
            continue
    prevNum = negative
    hitsCounter += 1

    
    
