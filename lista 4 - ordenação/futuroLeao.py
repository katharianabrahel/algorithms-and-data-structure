#função para ordenação merge sort
def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        i, j, k = 0, 0, 0

        while i < len(esquerda) and j < len(direita):
            if int(esquerda[i]) < int(direita[j]):
                lista[k] = int(esquerda[i])
                i += 1
            else:
                lista[k] = int(direita[j])
                j += 1
            k += 1
        
        while i < len(esquerda):
            lista[k] = int(esquerda[i])
            i += 1
            k += 1
        
        while j < len(direita):
            lista[k] = int(direita[j])
            j += 1
            k += 1
    
#funçõa pra achar a mediana
#se a quantidade elementos for impar, retorna o elemento do meio. se não tira a media entre os 2 elementos do meio
def calcular_mediana(lista):
    n = len(lista)
    if len(lista) % 2 != 0:
        mediana = lista[n//2]
    else:
        mediana = (lista[(n//2) - 1] + lista[n//2]) / 2
    return f"O salário sugerido por Juba na primeira negociação será de {mediana:.2f} mil reais."


salarios_sport = input().split()
salarios_outros = input().split()
todos_salarios = salarios_sport + salarios_outros
mergeSort(todos_salarios)
print(calcular_mediana(todos_salarios))