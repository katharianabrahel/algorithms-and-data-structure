class Node:
    def __init__(self, dado):
        #o nó possui seu valor e no máximo 2 filhos, um pra esquerda e outro pra direita
        self.valor = dado
        self.esq = None
        self.dir = None

class Arvore:
    #métodos add e search foram feitos baseados neste vídeo: https://youtu.be/VmKkAQtnjsM
    def __init__(self):
        self.raiz = None
    
    def add(self, dado):
        pai = None
        auxiliar = self.raiz
        #percorre a árvore, a partir da raiz, até o ponto que o novo nó será adicionado
        while auxiliar:
            pai = auxiliar
            if dado < auxiliar.valor:
                auxiliar = auxiliar.esq
            else:
                auxiliar = auxiliar.dir
        #confere se o nó será a raiz ou se ficará a esquerda ou a direita do pai
        if pai is None:
            self.raiz = Node(dado)
        elif dado < pai.valor:
            pai.esq = Node(dado)
        elif dado > pai.valor:
            pai.dir = Node(dado)
        
    def search(self, dado):
        return self._search(self.raiz, dado, 0)
        
    def _search(self, raiz, dado, altura):
        #se o valor não está na árvore, retorna -1. é conferido através do parâmetro raiz devido à recursão
        if raiz is None:
            return -1
        #retorna o parâmtro altura quando o parâmetro raiz for igual ao dado procurado
        elif raiz.valor == dado:
            return altura
        #percorre a árvore de forma recursiva, aumentando o valor da altura para cada nó percorrido
        elif dado < raiz.valor:
            return self._search(raiz.esq, dado, altura + 1)
        elif dado > raiz.valor:
            return self._search(raiz.dir, dado, altura + 1)
        

    def reordenar(self, dado):
        self.raiz = self._reordenar(self.raiz, dado)
    
    def _reordenar(self, raiz, dado):
        #se a raiz for vazia ou o valor buscado for igual a raiz, não há alterações
        if raiz is None or raiz.valor == dado:
            return raiz
        #confere se a nova raiz é maior ou menor que a raiz atual.
        #se for menor, realiza-se rotação simples a direita na subárvore da esquerda da raiz atual
        if dado > raiz.valor:
            raiz.dir = self._reordenar(raiz.dir, dado)
            raiz = self._rodarEsq(raiz)
        #se for maior, realiza-se rotação simples a esquerda na subárvore da direita da raiz atual
        elif dado < raiz.valor:
            raiz.esq = self._reordenar(raiz.esq, dado)
            raiz = self._rodarDir(raiz)

        return raiz

    def _rodarEsq(self, raiz):
        nova_raiz = raiz.dir
        raiz.dir = nova_raiz.esq
        nova_raiz.esq = raiz
        return nova_raiz
    

    def _rodarDir(self, raiz):
        nova_raiz = raiz.esq
        raiz.esq = nova_raiz.dir
        nova_raiz.dir = raiz
        return nova_raiz
    
arvore = Arvore()
fim = False
while not fim:
    try:
        comando = input().split()
        if comando[0] == 'ADD':
            arvore.add(int(comando[1]))
            print(arvore.search(int(comando[1])))
        elif comando[0] == 'SCH':
            altura = arvore.search(int(comando[1]))
            print(altura)
            #confere se o valor está na lista. se estiver, o valor se torna raiz e é feita a reordenação
            if altura != -1:
                arvore.reordenar(int(comando[1]))
    except EOFError:
        fim = True