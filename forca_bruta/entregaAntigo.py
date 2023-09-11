from itertools import permutations

arquivo = open('matriz.txt', 'r')

n, m = arquivo.readline().split() # pega o arquivo e divide em linhas e colunas n e m
linhas = arquivo.read().splitlines()

coordenadas = {}
pontoDeliver = []

for i in range(int(n)):
    line = linhas[i].split()
    for j in line:
        if j != '0':
            coordenadas[j] = (i, line.index(j))
            pontoDeliver.append(j)

pontoDeliver.remove('R')
custoDoMenorPercurso = float('inf')

for item in list(permutations(pontoDeliver)):
    current_cost = 0
    contador = 0

    item = list(item)
    item.append('R')
    item.insert(0, 'R')

    while contador < len(item)-1:
        y_cost = abs(coordenadas[item[contador]][0] - coordenadas[item[contador + 1]][0])
        x_cost = abs(coordenadas[item[contador]][1] - coordenadas[item[contador + 1]][1])
        current_cost += x_cost + y_cost
        contador += 1

 #calcular a rotar
    if current_cost < custoDoMenorPercurso:
        custoDoMenorPercurso = current_cost
        route = item

print(' '.join(route[1:-1]))