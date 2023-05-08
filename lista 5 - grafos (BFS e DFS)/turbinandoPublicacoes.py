def usar_boost(users, usuario, boost):
    #já adicionaa os seguidores do usuario na lista
    lista_atingidos = users[usuario]
    fila = users[usuario]
    #percorre cada seguidor do usuario
    for id in fila:
        #percorre os seguidores do seguidor em destaque
        for seguidores in users[id]:
            if boost < 5.25:
                return lista_atingidos
            if seguidores not in lista_atingidos and seguidores != usuario:
                lista_atingidos.append(seguidores)
                boost -= 5.25
    return lista_atingidos

    
n = int(input())
usuario = input()
boost = int(input())
#o dicionario 'users' representa o grafo, onde a chave é o vertice
#e o valor é uma lista de adjacencias
users = {}
for i in range(n):
    linha = input().split()
    users[linha[0]] = linha[2:]

print(usar_boost(users, usuario, boost))