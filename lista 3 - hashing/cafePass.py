class TabelaHash:
    def __init__(self, cpf, numero_magico):
        #a tabela possui 10 espaços para alocação dos digitos, de 0 a 9
        self.tabela = [None] * 10
        self.numero_magico = numero_magico
        for digito in cpf:
            indice = int(digito)
            #se o espaço a ser adicionado estiver vazio, adiciona o digito * 10. se não, soma o valor que já tem ao digito * 10
            if self.tabela[indice] is None:
                self.tabela[indice] = indice * 10
            else:
                self.tabela[indice] += indice * 10

        self.tabela_reduzida = []
        #cria uma nova tabela sem os espaços vazios
        for i in range(len(self.tabela)):
            if self.tabela[i] is not None:
                self.tabela_reduzida.append(self.tabela[i])
    
    def permissao(self):
        #cria um conjunto do números percorridos
        numeros_vistos = set()
        for numero in self.tabela_reduzida:
            #se houver intersseção entre o conjunto e a diferença entre o número mágico e o valor atual, retorna UP Permission
            #isso significa que existem 2 números em que a soma é o número mágico
            if (self.numero_magico - numero) in numeros_vistos:
                print('UP Permission')
                return
            #se não há intersseção, adiciona o valor atual à tabela de números visto
            numeros_vistos.add(numero)
        #se não houve intersseção entre o conjunto e nenhum valor da tabela, então retorna NOT Permission
        print('NOT Permission')


entradas = int(input())
for i in range(entradas):
    cpf, numero_magico = input().split()
    aluno = TabelaHash(cpf, int(numero_magico))
    aluno.permissao()