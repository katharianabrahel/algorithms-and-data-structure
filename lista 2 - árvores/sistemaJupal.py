class Node():
    def __init__(self, dado):
        #cada nó possui seu valor e no máximo 2 filhos, além de valor correspondente a altura
        self.valor = dado
        self.esq = None
        self.dir = None
        self.altura = 1

class AVL():
    #percorre a árvore de modo similar a busca binária, conferindo se será inserido a esquerda ou direita
    def inserir(self, raiz, dado):
        if not raiz:
            print(f'{dado} INSERIDO')
            return Node(dado)
        elif dado == raiz.valor:
            #não adiciona nomes repetidos a árvore
            print(f'{dado} JA EXISTE')
            return
        elif dado < raiz.valor:
            raiz.esq = self.inserir(raiz.esq, dado)
        else:
            raiz.dir = self.inserir(raiz.dir, dado)
        
        raiz.altura = 1 + max(self.altura_no(raiz.esq), self.altura_no(raiz.dir))

        #confere se a árvore está balanceada após a inserção de um novo elemento. deve rebalancear caso o fator de balanceamento seja maior que 1 ou menor que -1
        fator_balanceamento = self.balanceamento(raiz)
        if fator_balanceamento > 1:
            if dado < raiz.esq.valor:
                return self.rodarDir(raiz)
            else:
                raiz.esq = self.rodarEsq(raiz.esq)
                return self.rodarDir(raiz)
        if fator_balanceamento < -1:
            if dado > raiz.dir.valor:
                return self.rodarEsq(raiz)
            else:
                raiz.dir = self.rodarDir(raiz.dir)
                return self.rodarEsq(raiz)
            
        return raiz
    
    def deletar(self, raiz, dado):
        if not raiz:
            #o valor buscado não está na árvore
            print(f'{dado} NAO ENCONTRADO')
            return raiz
        #percorre a árvore até achar o valor a ser deletado
        elif dado < raiz.valor:
            raiz.esq = self.deletar(raiz.esq, dado)
        elif dado > raiz.valor:
            raiz.dir = self.deletar(raiz.dir, dado)
        else:
            if raiz.esq is None:
                temp = raiz.dir
                raiz = None
                print(f'{comando[1]} DELETADO')
                return temp
            elif raiz.dir is None:
                temp = raiz.esq
                raiz = None
                print(f'{comando[1]} DELETADO')
                return temp
            temp = self.minimo(raiz.dir)
            raiz.valor = temp.valor
            raiz.dir = self.deletar(raiz.dir, temp.valor)
        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura_no(raiz.esq), self.altura_no(raiz.dir))

        #confere se a árvore está balanceada após a remoção do elemento
        fator_balanceamento = self.balanceamento(raiz)
        if fator_balanceamento > 1:
            if self.balanceamento(raiz.esq) >= 0:
                return self.rodarDir(raiz)
            else:
                raiz.esq = self.rodarEsq(raiz.esq)
                return self.rodarDir(raiz)
        if fator_balanceamento < -1:
            if self.balanceamento(raiz.dir) <= 0:
                return self.rodarEsq(raiz)
            else:
                raiz.dir = self.rodarDir(raiz.dir)
                return self.rodarEsq(raiz)
        return raiz

    #função para rotacioar para esquerda
    def rodarEsq(self, no):
        y = no.dir
        T2 = y.esq
        y.esq = no
        no.dir = T2
        no.altura = 1 + max(self.altura_no(no.esq), self.altura_no(no.dir))
        y.altura = 1 + max(self.altura_no(y.esq), self.altura_no(y.dir))
        return y

    #função para rotacioar para direita
    def rodarDir(self, no):
        y = no.esq
        T3 = y.dir
        y.dir = no
        no.esq = T3
        no.altura = 1 + max(self.altura_no(no.esq), self.altura_no(no.dir))
        y.altura = 1 + max(self.altura_no(y.esq), self.altura_no(y.dir))
        return y 

    #achar altura do no
    def altura_no(self, no):
        if not no:
            return 0
        return no.altura
    
    #achar fator de balanceamento
    def balanceamento(self, raiz):
        if not raiz:
            return 0
        return self.altura_no(raiz.esq) - self.altura_no(raiz.dir)
    
    #achar o valor mínimo da árvore
    def minimo(self, raiz):
        if raiz is None or raiz.esq is None:
            return raiz
        return self.minimo(raiz.esq)
    
    #achar o valor máximo da árvore
    def maximo(self, raiz):
        if raiz is None or raiz.dir is None:
            return raiz
        return self.maximo(raiz.dir)

    #achar a altura da árvore    
    def altura_arvore(self, raiz):
        return 1 + max(self.altura_no(raiz.esq), self.altura_no(raiz.dir))
    
    #imprime o nó e seus filhos a partir da raiz, depois indo para esquerda e depois para direita. 
    #QUESTÃO EXTRA
    def ver(self, raiz):
        if raiz is not None:
            if raiz.esq is None and raiz.dir is None:
                print(f'{raiz.valor} não ajuda ninguém')
            elif raiz.esq is not None and raiz.dir is None:
                print(f'{raiz.valor} ajuda {raiz.esq.valor}')
            elif raiz.esq is None and raiz.dir is not None:
                print(f'{raiz.valor} ajuda {raiz.dir.valor}')
            elif raiz.esq is not None and raiz.dir is not None:
                print(f'{raiz.valor} ajuda {raiz.esq.valor} e {raiz.dir.valor}')
            self.ver(raiz.esq)
            self.ver(raiz.dir)

    #mesmo que a função ver mas pode começar a printar a partir de uma subarvore da raiz. 
    #QUESTÃO EXTRA        
    def ver_nome(self, raiz, dado):
        if dado == raiz.valor:
            self.ver(raiz)
        elif dado < raiz.valor:
            self.ver_nome(raiz.esq, dado)
        elif dado > raiz.valor:
            self.ver_nome(raiz.dir, dado)

#coloca os valores de cada nó em uma lista que será exibida no final. a exibição é feita em ordem (esquerda, raiz, direita)
def emOrdem(raiz, lista):
    if raiz is not None:
        emOrdem(raiz.esq, lista)
        lista.append(raiz.valor)
        emOrdem(raiz.dir, lista)

arvore = AVL()
raiz = None
fim = False
while not fim:
    comando = input().split()
    if comando[0] == 'INSERIR':
        raiz = arvore.inserir(raiz, comando[1])
    elif comando[0] == 'DELETAR':
        raiz = arvore.deletar(raiz, comando[1])
    elif comando[0] == 'MINIMO':
        minimo = arvore.minimo(raiz)
        if raiz:
            print(f'MENOR: {minimo.valor}')
        else:
            print('ARVORE VAZIA')
    elif comando[0] == 'MAXIMO':
        maximo = arvore.maximo(raiz)
        if raiz:
            print(f'MAIOR: {maximo.valor}')
        else:
            print('ARVORE VAZIA')
    elif comando[0] == 'ALTURA':
        if raiz is not None:
            print(f'ALTURA: {arvore.altura_arvore(raiz)}')
        else:
            print('ALTURA: 0')
    elif comando[0] == 'VER':
        if len(comando) == 1:
            arvore.ver(raiz)
        else:
            arvore.ver_nome(raiz, comando[1])
    elif comando[0] == 'FIM':
        fim = True
lista = []
emOrdem(raiz, lista)
if len(lista) !=0:
    print(*lista)
else:
    print('ARVORE VAZIA')