class Node:
    def __init__(self, dado):
        #lista duplamente encadeada
        self.dado = dado
        self.prox = None
        self.ant = None

class Caixa:
    def __init__(self):
        #criei dois nós vazios, um que vai receber os nomes e outro os pagamentos
        self.tamanho = 0
        self.nome_primeiro = None
        self.nome_ultimo = None
        self.pagamento_primeiro = None
        self.pagamento_ultimo = None
        self.valor = 0

    def entrou(self, nome, pagamento):
        nomes = Node(nome)
        pagamentos = Node(pagamento)
        if self.tamanho != 0:
            #adiciona nome e pagamento aos seus respectivos nós no final da lista (fila)
            nomes.ant = self.nome_ultimo
            self.nome_ultimo.prox = nomes
            self.nome_ultimo = nomes

            pagamentos.ant = self.pagamento_ultimo
            self.pagamento_ultimo.prox = pagamentos
            self.pagamento_ultimo = pagamentos
        else:
            #adiciona nome e pagamento à lista vazia
            self.nome_primeiro = nomes
            self.nome_ultimo = nomes

            self.pagamento_primeiro = pagamentos
            self.pagamento_ultimo = pagamentos
        self.tamanho += 1
    
    def proximo(self, n_caixa):
        nome_chamado = self.nome_primeiro
        pagamento_chamado = self.pagamento_primeiro
        print(f'{nome_chamado.dado} foi chamado para o caixa {n_caixa}')
        #adiciona o valor do pagamento ao total do caixa
        self.valor += float(pagamento_chamado.dado)
        #o sucessor torna-se o primeiro da lista e o tamanho da fila diminui em 1
        self.nome_primeiro = self.nome_primeiro.prox
        self.pagamento_primeiro = self.pagamento_primeiro.prox
        self.tamanho -= 1
            
    def realocar_fila(self, n_caixa):
        #n_caixa indica o caixa vazio e caixa_adicional o caixa que cederá metade as pessoas
        if n_caixa == "1":
            caixa_adicional = caixa_2
        elif n_caixa == "2":
            caixa_adicional = caixa_1
        
        #soma o tamanho da lista + 1 para arredondar pra cima ao fazer a divisão inteira por 2
        meio = (caixa_adicional.tamanho + 1) // 2
        nome_adicional = caixa_adicional.nome_ultimo
        pagamento_adicional = caixa_adicional.pagamento_ultimo

        for i in range(meio):
            #adiciona os elementos do fim da lista não vazia para a vazia até chegar na metade
            self.entrou(nome_adicional.dado, pagamento_adicional.dado)
            nome_adicional = nome_adicional.ant
            pagamento_adicional = pagamento_adicional.ant
            #o antecessor ao elemento do meio se tornará o último elemento da lista que foi esvaziada pela metade
            caixa_adicional.nome_ultimo = caixa_adicional.nome_ultimo.ant
            caixa_adicional.pagamento_ultimo = caixa_adicional.pagamento_ultimo.ant
            caixa_adicional.tamanho -= 1


caixa_1 = Caixa()
caixa_2 = Caixa()

fim = False
while not fim:
    comando = input().split()
    if comando[0] == "ENTROU:":
        if comando[2] == "1":
            caixa_1.entrou(comando[1], comando[-1])
            print(f'{comando[1]} entrou na fila 1')
        elif comando[2] == "2":
            caixa_2.entrou(comando[1], comando[-1])
            print(f'{comando[1]} entrou na fila 2')
    elif comando[0] == "PROXIMO:":
        if comando[1] == "1":
            if caixa_1.tamanho != 0:
                caixa_1.proximo(comando[1])
            else:
                #só há necessidade de realocar se o caixa chamado estiver vazio
                caixa_1.realocar_fila(comando[1])
                caixa_1.proximo(comando[1])
        elif comando[1] == "2":
            if caixa_2.tamanho != 0:
                caixa_2.proximo(comando[1])
            else:
                caixa_2.realocar_fila(comando[1])
                caixa_2.proximo(comando[1])
    elif comando[0] == "FIM":
        fim = True

print(f'Caixa 1: R$ {caixa_1.valor:.2f}, Caixa 2: R$ {caixa_2.valor:.2f}')