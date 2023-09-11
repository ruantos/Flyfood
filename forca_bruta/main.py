import time
from matplotlib import pyplot as plt
def ler_matriz(nome_arquivo):

    """ Lê a matriz 'nome', retorna a matriz, os pontos na lista coordenada e a coordenada do ponto R """

    with open(nome_arquivo, 'r') as arquivo:
        n, m = [int(i) for i in arquivo.readline().split()]
        matrix = [list(linha.split()) for linha in arquivo]
    
    coordenadas = []            # Receberá a coordenada de todos os pontos na matriz fora o R. 

    for linha in range(n):
        for coluna in range(m):
            if matrix[linha][coluna] != '0':
                if matrix[linha][coluna] == 'R':
                    r = (linha, coluna)
                else:
                    ponto = (linha, coluna)
                    coordenadas.append(ponto)

    return matrix, coordenadas, r


def permutar(lista):
    if len(lista) <= 1:
        return [lista]
    
    permutacoes = []
    for i in range(len(lista)):
        chave = lista[i]
        resto = lista[:i] + lista[i + 1:]
        for p in permutar(resto):
            permutacoes.append([chave] + p)

    return permutacoes


def add_r(lista, R):
    """ Adiciona a coordenada do ponto R no começo e final da lista recebida"""
    for j in lista:
        j.append(R)
        j.insert(0, R)
    return lista


def distancia(percurso):
    """ Calcula a distância entre dois pontos de cada par consecutivo de pontos e soma-os"""
    distancia_total = 0
    d = 0

    for atual in range(1,len(percurso)):
        p1 = percurso[atual - 1]
        p2 = percurso[atual]
        d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])   #Calcula dist entre o ponto atual e anterior (atual-1)
        distancia_total += d

    return distancia_total


def grafico(E, T):
    """ Exibe o gráfico de crescimento da função flyfood.\n
    Sendo o eixo x referente a lista E, que contém o número de entradas de cada matriz testada e\n
    o eixo y referente a lista T, que contém o tempo de execução de cada matriz testada. 
    """
    plt.plot(E, T)
    plt.title('CRESCIMENTO DO FLYFOOD')
    plt.xlabel('ENTRADA(n)')
    plt.ylabel('TEMPO(s)')
    plt.show()


def main(nome, entrada_atual, tempo_atual):
    tic = time.process_time()           #Começa marcação de tempo

    matriz, coordenadas, coordenada_R = ler_matriz(nome) 
    permutacoes = permutar(coordenadas)
    
    menor_distancia = float('inf')       
    menor_percurso = None
    for percurso in add_r(permutacoes, coordenada_R):      #Adiciona R a cada percurso e compara-os.
        dist = distancia(percurso)                           
        if dist < menor_distancia:
            menor_distancia = dist
            menor_percurso = percurso

    for i in menor_percurso:                        #Printa as letras do percurso ótimo e a sua distancia.
        print(f'{matriz[i[0]][i[1]]}',end=' ')
    print(f'\nMenor distância: {menor_distancia}')

    toc = time.process_time()                         #Termina marcação de tempo
    print(f'Número de pontos: {len(menor_percurso) -1}')
    print(f'Tempo de execução: {toc - tic:.5f}(s)\n')
    
    tempo_atual.append(toc - tic)                       #Armazena o tempo e o número de entradas atual.
    entrada_atual.append(len(menor_percurso) -1)


if __name__ == '__main__':

    entradas = []   #receberá o n de pontos de cada matriz.
    tempos = []     # receberá o tempo de execução de cada matriz. 

    arquivos_teste = [
        'matriz1.txt',
        'matriz2.txt',
        'matriz3.txt',
        'matriz4.txt',
        'matriz5.txt']

    for arquivo in arquivos_teste:          #roda o programa para cada matriz na lista.
        main(arquivo, entradas, tempos)
        
    grafico(entradas, tempos)               #exibe o gráfico do crescimento de funções
