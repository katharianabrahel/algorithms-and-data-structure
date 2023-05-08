class TabelaHash:
    def __init__(self, tamanho):
        #cria uma lista com elementos vazios representando a memoria
        self.tabela = [None] * tamanho

    def add(self, dado):
        for i in range(len(self.tabela)):
            #o espaço da memoria a ser adicionado é calculado por dado mod qtd_memoria
            #caso o espaço esteja preenchido, irá procurar o próximo espaço a ser alocado na memoria. para isso, somei o valor de i ao dado na hora de fazer o mod
            indice = (dado + i) % len(self.tabela)
            if self.tabela[indice] is None:
                self.tabela[indice] = dado
                print(f'E: {indice}')
                return
        print("Toda memoria utilizada")       

    def search(self, dado):
        for i in range(len(self.tabela)):
            #percorre a memoria de forma similar ao metodo add
            #caso o valor seja None enquanto percorre a memoria, então o dado não foi inserido
            indice = (dado + i) % len(self.tabela)
            if self.tabela[indice] is not None:
                if self.tabela[indice] == dado:
                    print(f'E: {indice}')
                    return
            else:
                print("NE")
                return
        print("NE")

    def consultar_memoria(self, indice):
        if self.tabela[indice] is not None:
            print(f"A: {self.tabela[indice]}")
        else:
            print("D")

qtd_memoria = int(input())
qtd_comandos = int(input())

tabela = TabelaHash(qtd_memoria)

for i in range(qtd_comandos):
    comando, valor = input().split()
    if comando == "ADD":
        tabela.add(int(valor))
    elif comando == "SCH":
        tabela.search(int(valor))
    elif comando == "CAP":
        tabela.consultar_memoria(int(valor))