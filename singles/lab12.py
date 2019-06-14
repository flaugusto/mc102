# Este programa foi criado para interceptar as postagens feitas na rede social FACESTAR.
# Através de postagens do nosso informante infiltrado, podemos descobrir com o programa quais direções e elevações
# dos nossos canhões devemos utilizar para atacarmos as bases da império antes que nos ataquem.
# Entrada: Um texto de no máximo 1000 caracteres sendo a postagem no FACESTAR.
# Saída: As direções e elevações de cada base identificada no texto, uma em cada linha.

# Nome: Flavio Augusto Pereira Cunha
# RA: 197083

# Função principal de execução do programa
def main():
    # Entrada da postagem no FACESTAR
    post = input()
    post = post.lower() # transforma para minúsculo ignorando o estado das letras

    directions = findDirections(post)
    # Para cada direção encontrada:
    for direction in directions:
        # Encontra qual a elevação imediatamente posterior à ela, com base em sua posição
        elevation = findElevation(direction['position'], post)
        # Exibe o par de direção e elevação
        print(direction['name'] + ' - ' + elevation['name'])

# Função que procura as palavras chave de direções no texto e retorna suas posições na ordem em que foram encontradas
# @param text:string texto do post para análise
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

# Função que procura as palavras-chave de elevações e retorna a mais próxima da posição fornecida
# @param begin:int Posição inicial onde deve-se começar a procurar as elevações
# @param text:string texto do post para análise
def findElevation(begin, text):
    # Dicionário palavras-chave > ângulos de elevação
    elevations = {
        'verde': '30',
        'amarelo': '45',
        'vermelho': '60'
    }
    # Cria um item inicial de posição mais próxima sendo a mais longe possível
    nearElevation = {'position': len(text), 'elevation': 0 }
    # Para cada elevação encontrada:
    for key, elevation in elevations.items():
        pos = text.find(key, begin)
        if (pos != -1):
            # Verifica se a posição da elevação encontrada é menor que a anterior:
            if (pos < nearElevation['position']):
                # Atualiza esta como a menor se caso verdadeiro
                nearElevation['position'] = pos
                nearElevation['name'] = elevation
    # Assim, a função retornará sempre a elevação mais próxima encontrada, isto é, a imediatamente posterior a direção
    return nearElevation
    
# Invocação da função principal
main()