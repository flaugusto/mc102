# Este programa foi criado para interceptar as postagens feitas na rede social FACESTAR.
# Através de postagens do nosso informante infiltrado, podemos descobrir com o programa quais direções e elevações
# dos nossos canhões devemos utilizar para atacarmos as bases da império antes que nos ataquem.
# Entrada: Um texto de no máximo 1000 caracteres sendo a postagem no FACESTAR.
# Saída: As direções e elevações de cada base identificada no texto, uma em cada linha.

# Nome: Flavio Augusto Pereira Cunha
# RA: 197083

# Função principal que monta a saída com base na entrada
def main():
    # Entrada da postagem no FACESTAR
    post = input()
    post = post.lower() # ignorando maiúsculas ou minúsculas

    directions = findDirections(post)
    for direction in directions:
        elevation = findElevation(direction['position'], post)
        print(direction['name'] + ' - ' + elevation['name'])

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
                'name': direction,
                'position': pos
            }
            # E salva a posição encontrada junto com a direção correspondente
            positions.append(item)
            start = pos + 1
    # Ordena a lista de direções de acordo com a ordem que apareceram no texto
    positions.sort(key = lambda pair: pair['position'])
    return positions

# Função que procura as palavras-chave de elevações e retorna a mais próxima a posição fornecida
def findElevation(pos, text):
    # Dicionário palavras-chave > ângulos de elevação
    elevations = {
        'verde': '30',
        'amarelo': '45',
        'vermelho': '60'
    }
    nearElevation = {'position': len(text), 'elevation': 0 }
    for key, elevation in elevations.items():
        elePos = text.find(key, pos)
        if (elePos != -1):
            if (elePos < nearElevation['position']):
                nearElevation['position'] = elePos
                nearElevation['name'] = elevation
    return nearElevation

main()