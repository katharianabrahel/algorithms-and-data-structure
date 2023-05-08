def pilhaImaculada(pilha):
    #conferir se a pilha está ordenada
    for i in range(1, len(pilha)):
        if int(pilha[i]) < int(pilha[i-1]):
            return False
    return True

def novaLocacao(pilha, codigo):
    ordenada = pilhaImaculada(pilha)
    if not ordenada:
        print("A pilha está um caos.")
    else:
        #achar a posição que a nova locação será inserida sem desordenar a lista
        indice = 0
        while indice < len(pilha) and int(pilha[indice]) < int(codigo):
            indice += 1
        pilha.insert(indice, codigo)
        print(pilha)

solicitacoes = list(input().split(','))
nova_locacao = input()
novaLocacao(solicitacoes, nova_locacao)