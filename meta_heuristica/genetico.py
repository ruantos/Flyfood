import random
from matplotlib import pyplot as plt
import time


class Cidade:
    """ Inicia a cidade com as coordenadas, deve receber tupla com x e y"""
    def __init__(self, coordenadas, indice):
        self.nome = indice
        self.x = coordenadas[0]
        self.y = coordenadas[1]


class Individuo:
    """Inicia uma rota, deve receber uma lista com os objetos cidade"""
    def __init__(self, cidades=None, permutar=True):
        if permutar:
            self.rota = random.sample(cidades, len(cidades))
        else:
            self.rota = cidades
        self.fitness = None
        self.custo = None


    def __repr__(self):
        s = ""
        for cidade in self.rota:
            s += f"({cidade.x}, {cidade.y}) "
        return s


    def ifitness(self):
        """Calcula o fitness de cada individuo à partir da soma das distâncias euclidianas"""
        custo_total = 0
        percurso = self.rota

        for cidade in range(len(percurso)):
            if cidade < (len(percurso) -1):
                # Soma as distancias da primeira até a última cidade
                custo_total += distEuclidiana(percurso[cidade], percurso[cidade + 1])
            else:
                # Soma a distância da última cidade para a primeira.
                custo_total += distEuclidiana(percurso[cidade], percurso[0])

        self.fitness = 1 / custo_total
        self.custo = custo_total


def lerCoordenadas(arquivo, coordenadas):
    with open(arquivo, "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            cidade_indx = int(partes[0])
            x = float(partes[1])
            y = float(partes[2])
            coordenadas[cidade_indx] = (x, y)


def criarCidades(coordenadas):
    lista = []
    for indx, (x, y) in coordenadas.items():
        lista.append(Cidade((x,y), indx))
    return lista


def distEuclidiana(cidade1, cidade2):
    """Calcula a distância entre as cidades com a fórmula de distância euclidiana"""
    return ((cidade2.x - cidade1.x)**2 + (cidade2.y - cidade1.y)**2) **0.5


def comparaAdd(lista, individuo):
    for objeto in lista:
        if objeto.rota == individuo.rota:
            return
    lista.append(individuo)


def popInicial(cidades ,tamanho_populacao):
    """Cria população inicial com quantidade x de indíviduos """
    populacao = []
    while len(populacao) != tamanho_populacao:
        individuo = Individuo(cidades)
        comparaAdd(populacao, individuo)
    return populacao


def fitPopulacao(populacao):
    """Calcula e armazena o fitness de toda a população"""
    for individuo in populacao:
        individuo.ifitness()


def torneio(populacao, tamanho_populacao):
    """ Seleção por Torneio"""
    pais = [0 for _ in range(tamanho_populacao)]


    for torneio in range(tamanho_populacao):
        indice1 = random.randint(0, len(populacao) -1)
        indice2 = random.randint(0, len(populacao) -1)
        
        if populacao[indice1].fitness > populacao[indice2].fitness:
            pais[torneio] = populacao[indice1]
        else:
            pais[torneio] = populacao[indice2]
            
    return pais


def isHere(gene, individuo):
    """Para verificar se um individuo tem determinado gene"""
    for cidade in individuo:
        if cidade.x == gene.x and cidade.y == gene.y:
            return True
    return False


def crossIndividuo(pai1, pai2, taxa_crossover):
    """Função para gerar novos individuos a partir de dois pais selecionados"""
    sorteio = random.random() 
    if sorteio < taxa_crossover:
        genesP1 = []    
        genesP2 = []    
        
        geneA = int(random.randint(0, len(pai1.rota)))  
        geneB = int(random.randint(0, len(pai1.rota)))  

        comeco = min(geneA, geneB)
        fim = max(geneA, geneB)

        for i in range(comeco, fim):
            genesP1.append(pai1.rota[i])

        for cidade in pai2.rota:
            if not isHere(cidade, genesP1):
                genesP2.append(cidade)

        filho1 = genesP1 + genesP2
        filho1 = Individuo(filho1, False)
        
        filho2 = genesP2 + genesP1
        filho2 = Individuo(filho2, False)
        
        return filho1, filho2
    return pai1, pai2 


def crossPopulacao(pais, n_populacao, taxa_crossover):
    """Faz o crossover com os pais selecionados pelo torneio"""
    filhos = ["" for i in range(n_populacao)]

    for crossover in range(0, n_populacao, 2):
        pai1 = pais[crossover]
        pai2 = pais[crossover + 1]

        filho1, filho2 = (crossIndividuo(pai1, pai2, taxa_crossover))
        filhos[crossover] = filho1
        filhos[crossover + 1] = filho2
    return filhos


def mutacaoIndv(individuo, taxa_mutacao):
    """ Mutação de um filho"""
    if random.random() < taxa_mutacao:
        pos1 = random.randint(0, len(individuo.rota) - 1)
        pos2 = random.randint(0, len(individuo.rota) - 1)
        
        while pos2 == pos1:
            pos2 = random.randint(0, len(individuo.rota) - 1)
        
        individuo.rota[pos1], individuo.rota[pos2] = individuo.rota[pos2], individuo.rota[pos1]
    return individuo


def mutacaoPop(filhos, taxa_mutacao):
    """Mutação de todos os filhos"""
    for idx, individuo in enumerate(filhos):
        filhos[idx] = mutacaoIndv(individuo, taxa_mutacao)
    return filhos


def melhorIndv(pais, geracao, geracoes, lista):
    max_fitness = 0
    
    for indx, indv in enumerate(pais):
        if indv.fitness > max_fitness:
            max_indx = indx


    if geracao == geracoes - 1:
        print(f"Geração {geracao + 1}, Melhor fitness: {pais[max_indx].custo }") 
    else:
        print(f"Geração {geracao + 1}, Melhor fitness: {pais[max_indx].custo }")

    lista.append(pais[max_indx].custo)


def geracoes(pop, taxa_crossover, taxa_mutacao, n_pop, n_geracoes):
    lista_fitness = []          #Armazenará o melhor fitness de cada geração.
    for geracao in range(n_geracoes):
        fitPopulacao(pop)
        parents = torneio(pop, n_pop)
        children = crossPopulacao(parents, n_pop, taxa_crossover)
        mutacaoPop(children, taxa_mutacao)
        pop = children  # Atualize a população atual com os filhos gerados
        fitPopulacao(pop)  # Recalcule o fitness após a mutação
        parents = torneio(pop, n_pop)  # Selecione novos pais para a próxima geração
        # Imprima ou armazene informações sobre a geração, se necessário
        melhorIndv(parents, geracao, n_geracoes, lista_fitness)
    
    plt.plot([i for i in range(0, n_geracoes)], lista_fitness)
    plt.show()



def principal():
    random.seed(45)


    # lenght_pop = 200    # Tamanho da população
    # taxa_crossover = 0.6   # Taxa de crossover
    # taxa_mutacao = 0.0045   # Taxa de mutação
    # n_geracoes = 1_000  # Número de gerações

    lenght_pop = 500    # Tamanho da população
    taxa_crossover = 0.45   # Taxa de crossover
    taxa_mutacao = 0.005   # Taxa de mutação
    n_geracoes = 2_500  # Número de gerações



    tic = time.time()
    coordenadas = {}
    # arquivo = "berlin52.txt"
    # arquivo = "bays29.txt"
    arquivo = "ts225.txt"


    lerCoordenadas(arquivo, coordenadas)
    cities = criarCidades(coordenadas)  #Transforma  as coordenadas em objetos cidade e guarda na lista 
    initial_pop = popInicial(cities, lenght_pop)  # Gera a população inicial
    geracoes(initial_pop, taxa_crossover, taxa_mutacao, lenght_pop, n_geracoes) #Começa a evolução
    toc = time.time()
    print(f'Tempo de execução {toc - tic}')


principal()

