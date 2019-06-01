# Sistema da DAC
# Este programa consegue fazer algumas operações com os RA's utilzados como identificação de alunos da UNICAMP
# As operações são: Imprimir, Ordernar, Remover, Inserir e Buscar
# Os comandos são dados por letras seguidas dos parametros para cada comando, como segue:
# Entrada:
# n inteiros no padrão de RA da Unicamp
# p - Imprime a lista completa de alunos
# c - ordenação crescente
# d - ordenação decrescente
# b - busca binária <ra_busca>
# i - inserção <ra_insercao>
# r - remoção <ra_remocao>
# s - sair do programa
# Saída:
# Para cada comando 'p' enviado, deve ser exibido a lista atual, após as devidas operações.
# No caso de busca binária, cada passo de sua execução também serão exibidos.

# Nome: Flavio Augusto Pereira Cunha
# RA: 197083


def main():
    # entrada da lista de RA's
    line = input().split()
    students = [int(x) for x in line]

    cmd = ['']
    sortedAsc = ''
    # Até que o comando enviado seja de 'saída', continue a execução do programa
    while cmd[0] != 's':
        cmd = input().split()
        if len(cmd) > 1:
            cmd[1] = int(cmd[1])
        if cmd[0] == 'p':
            printArray(students)
        if cmd[0] == 'c':
            students.sort()
            sortedAsc = 'True'
        if cmd[0] == 'd':
            students.sort(reverse = True)
            sortedAsc = 'False'
        if cmd[0] == 'b':
            binarySearch(cmd[1], students, sortedAsc, False)
        if cmd[0] == 'i':
            insert(cmd[1], students, sortedAsc)
        if cmd[0] == 'r':
            remove(cmd[1], students)


def printArray(array):
    if len(array) > 0:
        for item in array:
            print(str(item) + ' ', end='')
        print()

def binarySearch(key, array, sortedAsc, quiet):
    # Testa se a lista está ordenada
    if sortedAsc == '':
        print("Vetor nao ordenado!")
        return
    i = 0 # pos inicial
    f = len(array) - 1 # pos final
    while i <= f:
        m = (f + i) // 2 # pos media
        if not quiet:
            print(m, end = ' ')
        if array[m] == key:
            if not quiet:
                print()
                print("%d esta na posicao: %d"%(array[m], m))
            return m
        if sortedAsc == 'False':
            if key > array[m]:
                f = m - 1
            else:
                i = m + 1
        else:
            if key < array[m]:
                f = m - 1
            else:
                i = m + 1
    if not quiet:
        print()
        print("%d nao esta na lista!" % key)
    return -1

def insert(item, array, sortedAsc):
    # Se o vetor já tiver atingido o max, não insere e exibe a mensagem
    maxLength = 150
    if maxLength < len(array) + 1:
        print("Limite de vagas excedido!")
        return
    # Se o aluno já estiver na lista
    if exists(item, array):
        print("Aluno ja matriculado na turma!")
        return
    # Com o vetor não ordenado, insere no fim da lista
    if sortedAsc == '':
        array.append(item)
        return array
    # Se o vetor está ordenado, insere e ordena da forma que estava
    elif sortedAsc == 'True':
        array.append(item)
        array.sort()
        return array
    elif sortedAsc == 'False':
        array.append(item)
        array.sort(reverse = True)
        return array

def exists(item, array):
    if item in array:
        return True
    else:
        return False

def remove(item, array):
    # Se não tiver mais nenhum aluno na lista, não faz a remoção
    if not len(array) > 0:
        print("Nao ha alunos cadastrados na turma!")
        return
    # Se o item existir na lista, acha seu indice e o remove
    if exists(item, array):
        array.remove(item)
        return
    else:
        print("Aluno nao matriculado na turma!")
        return

main()
