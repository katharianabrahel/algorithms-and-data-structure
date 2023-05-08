def soma_maxima(n, nums):
    #se tiver só um setor, retorna ele mesmo
    if n == 1:
        return nums[0]
    #cria a lista de somas máximas possíveis
    total = [0] * n
    #a primeira soma é o primeiro elemento
    total[0] = nums[0]
    #a segunda soma máxima é o maior entre o primeiro e o segundo elemento
    total[1] = max(nums[0], nums[1])
    for i in range(2, n):
        #percorre os setores a partir do terceiro elemento
        #atualiza a lista com o max entre a soma máxima sem incluir o valor atual e soma máxima incluindo o valor atual sem contabilizar os adjacentes
        total[i] = max(total[i-1], total[i-2] + nums[i])
    #a maior soma possível será o último elemento da lista
    return total[-1]


n = int(input())
qtd_torcedores = list(map(int, input().split()))

fotografados = soma_maxima(n, qtd_torcedores)

print(f"{fotografados} torcedores podem ser fotografados.")