class Node:
    def __init__(self, dado):
        #como é uma lista duplamente encadeada, a classe tem o valor do nó e do seu sucessor e antecessor
        self.dado = dado
        self.prox = None
        self.ant = None

class Historico:
    def __init__(self):
        #a lista começa vazia
        self.tamanho = 0
        self.primeiro = None
        self.ultimo = None

    def add(self, busca):
        node = Node(busca)
        if self.tamanho == 0:
            #adiciona o nó na lista vazia
            self.primeiro = node
            self.ultimo = node
        else:
            #adicionando item numa estrutura de pilha
            node.prox = self.primeiro
            self.primeiro.ant = node
            self.primeiro= node
        self.tamanho += 1
    
    def remove(self, busca):
        #faz a busca na lista a partir do seu primeiro elemento
        node = self.primeiro
        while node is not None:
            if node.dado == busca:
                #confere se o dado a ser removido é o primeiro item da lista
                if node.ant is not None:
                    #não é o primeiro da lista. desconecta o nó do seu antecessor ao conectar o antecessor com o sucessor
                    node.ant.prox = node.prox
                else:
                    #é o primeiro da lista. o sucessor se torna o primeiro elemento da lista
                    self.primeiro = node.prox
                #confere se o dado a ser removido é o último item da lista
                if node.prox is not None:
                    #não é o último da lista. desconecta o nó do seu sucessor ao conectar o sucessor com o antecessor
                    node.prox.ant = node.ant
                else:
                    #é o primeiro da lista. o antecessor se torna o último elemento da lista
                    self.ultimo = node.ant
                self.tamanho -= 1
                return
            #repete a busca para o próximo nó
            node = node.prox

    def find(self, busca):
        #juntei a função remove com a função add, assim desconecto o nó da lista e adiciono-o no início
        node = self.primeiro
        while node is not None:
            if node.dado == busca:
                if node.ant is not None:
                    node.ant.prox = node.prox
                else:
                    self.primeiro = node.prox
                if node.prox is not None:
                    node.prox.ant = node.ant
                else:
                    self.ultimo = node.ant
                node.prox = self.primeiro
                node.ant = None
                self.primeiro.ant = node
                self.primeiro = node
                return
            node = node.prox

    def exibir(self):
        #percorre a lista a partir do primeiro elemento, printando cada um
        node = self.primeiro
        while node is not None:
            print(node.dado)
            node = node.prox

    
historico = Historico()
fim = False 
while not fim:
    entrada = input().split()
    if entrada[0] == "ADD":
        historico.add(entrada[-1])
    elif entrada[0] == "REM":
        historico.remove(entrada[-1])
    elif entrada[0] == "FIND":
        historico.find(entrada[-1])
    elif entrada[0] == "EXIB":
        historico.exibir()
    elif entrada[0] == "END":
        fim = True