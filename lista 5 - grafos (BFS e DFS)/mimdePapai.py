def qtd_usuarios (grafo, vistos, id):
    #i- 1 por conta do intervalo 1 <= i <= n
    #então é necessário diminuir 1 para o indice corresponder ao vértice do grafo
    vistos[id - 1] = True
    #visualizacoes começa em 1 já que conta o próprio vértice
    n_visualizacoes = 1
    for adjacentes in grafo[id]:
        if not vistos[adjacentes - 1]:
            n_visualizacoes += qtd_usuarios(grafo, vistos, adjacentes)
    return n_visualizacoes
    
    
usuarios, conexoes = map(int, input().split())
#o dicionario 'graph' representa o grafo, onde a chave é o vertice
#e o valor é uma lista de adjacencias
graph = {i: [] for i in range(1, usuarios + 1)}

for i in range(conexoes):
    u, v = map(int, input().split())
    #cada chave recebe o valor do outro
    graph[u].append(v)
    graph[v].append(u)

total = [0] * usuarios
for i in range(usuarios):
    #para cada elemento, cria-se uma lista de boleanos para indicar se o vértice já foi visitado
    vistos = [False] * usuarios
    #i + 1 pois o intervalo é de 1 <= i <= n
    total[i] = qtd_usuarios(graph, vistos, i + 1)

print(*total)