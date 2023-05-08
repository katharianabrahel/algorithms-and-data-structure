'''
As funções de ordenação, sem usar o limite máximo de ações, irão retornar uma tupla com número de comparações e o número de trocas
Quando tem limite, sempre irá conferir, após uma comparação ou uma troca, se a soma de das comparações com as trocas é maior ou igual ao limite.
'''

def bubble_sort(lista, limite):
    n = len(lista)
    comp = 0
    trocas = 0
    for i in range(n):
        for j in range(n - i - 1):
            comp += 1
            if limite is not None:
                if (comp + trocas) >= limite:
                    return print(f"Com {comp + trocas} ações, Caça-Rato ordena a lista assim: {lista}")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
            if limite is not None:
                if (comp + trocas) >= limite:
                    return print(f"Com {comp + trocas} ações, Caça-Rato ordena a lista assim: {lista}")
    return comp, trocas

def selection_sort(lista, limite):
    n = len(lista)
    comp = 0
    trocas = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comp += 1
            if limite is not None:
                if (comp + trocas) >= limite:
                    return print(f"Com {comp + trocas} ações, Grafite ordena a lista assim: {lista}")
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
        if i != min_index:
            trocas += 1
        if limite is not None:
            if (comp + trocas) >= limite:
                return print(f"Com {comp + trocas} ações, Grafite ordena a lista assim: {lista}")
    return comp, trocas

def insertion_sort(lista, limite):
    n = len(lista)
    comp = 0
    trocas = 0
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > key:
            if lista[j + 1] != lista[j]:
                trocas += 1
                if limite is not None:
                    if (comp + trocas) >= limite:
                        return print(f"Com {comp + trocas} ações, Lacraia ordena a lista assim: {lista}")
            lista[j + 1] = lista[j]
            j -= 1
            comp += 1
            if limite is not None:
                if (comp + trocas) >= limite:
                    return print(f"Com {comp + trocas} ações, Lacraia ordena a lista assim: {lista}")
        if j != -1:
            comp += 1
        lista[j + 1] = key
        if limite is not None:
            if (comp + trocas) >= limite:
                return print(f"Com {comp + trocas} ações, Lacraia ordena a lista assim: {lista}")
    return comp, trocas

def shell_sort(lista, limite):
    n = len(lista)
    gap = n // 2
    comp = 0
    trocas = 0
    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:
                comp += 1
                if limite is not None:
                    if (comp + trocas) >= limite:
                        return print(f"Com {comp + trocas} ações, Rivaldo ordena a lista assim: {lista}")
                if lista[j] != lista[j - gap]:
                    trocas += 1
                lista[j] = lista[j - gap]
                j -= gap
                if limite is not None:
                    if (comp + trocas) >= limite:
                        return print(f"Com {comp + trocas} ações, Rivaldo ordena a lista assim: {lista}")
            lista[j] = temp
            if lista[j] != temp:
                trocas += 1
                if limite is not None:
                    if (comp + trocas) >= limite:
                        return print(f"Com {comp + trocas} ações, Rivaldo ordena a lista assim: {lista}")
            if j >= gap and lista[j - gap] != temp:
                comp += 1
            if limite is not None:
                if (comp + trocas) >= limite:
                    return print(f"Com {comp + trocas} ações, Rivaldo ordena a lista assim: {lista}")
        gap //= 2
    return comp, trocas

def quicksort(A, lo, hi):
    global comp_quick, trocas_quick
    if lo >= 0 and hi >= 0 and lo < hi:
      p = partition(A, lo, hi)
      quicksort(A, lo, p)
      quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    global comp_quick, trocas_quick
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    while True:
      if i >= j:
        return j
      while A[i] < pivot:
        comp_quick += 1
        i += 1
      while A[j] > pivot:
        comp_quick += 1
        j -= 1
      A[i], A[j] = A[j], A[i]
      trocas_quick += 1


numeros = list(map(int, input().split()))

contagem_bubble = bubble_sort(numeros.copy(), limite=None)
contagem_selection = selection_sort(numeros.copy(), limite=None)
contagem_insertion = insertion_sort(numeros.copy(), limite=None)
contagem_shell = shell_sort(numeros.copy(), limite=None)
comp_quick = 0
trocas_quick = 0
quicksort(numeros.copy(), 0, len(numeros) - 1)

print(f"Caça-Rato ordena a lista com {contagem_bubble[0]} comparações e {contagem_bubble[1]} trocas.")
print(f"Grafite ordena a lista com {contagem_selection[0]} comparações e {contagem_selection[1]} trocas.")
print(f"Lacraia ordena a lista com {contagem_insertion[0]} comparações e {contagem_insertion[1]} trocas.")
print(f"Rivaldo ordena a lista com {contagem_shell[0]} comparações e {contagem_shell[1]} trocas.")
print(f"Toninho ordena a lista com {comp_quick} comparações e {trocas_quick} trocas.")
print("-VENCEDOR DA RODADA-")

#dicionário com o nome dos jogadores e o total de ações feita por cada algoritmo
n_acoes = {"Caça-Rato": contagem_bubble[0] + contagem_bubble[1], 
          "Grafite": contagem_selection[0] + contagem_selection[1], 
          "Lacraia": contagem_insertion[0] + contagem_insertion[1], 
          "Rivaldo": contagem_shell[0] + contagem_shell[1], 
          "Toninho": comp_quick + trocas_quick}

#acha o vencedor pelo minimo de ações
vencedor = min(n_acoes, key=n_acoes.get)
print(f"O vencedor da rodada é {vencedor}, com {n_acoes[vencedor]} ações.")
print("-Toninho está a dormir...-")
print("Os outros estagiários retornam as seguintes listas com essa quantidade de ações:")

#faz a ordenação para cada caso usando o limite de ações do vencedor
if vencedor == "Caça-Rato":
    selection_sort(numeros.copy(), n_acoes[vencedor])
    insertion_sort(numeros.copy(), n_acoes[vencedor])
    shell_sort(numeros.copy(), n_acoes[vencedor])
    
elif vencedor == "Grafite":
    bubble_sort(numeros.copy(), n_acoes[vencedor])
    insertion_sort(numeros.copy(), n_acoes[vencedor])
    shell_sort(numeros.copy(), n_acoes[vencedor])

elif vencedor == "Lacraia":
    bubble_sort(numeros.copy(), n_acoes[vencedor])
    selection_sort(numeros.copy(), n_acoes[vencedor])
    shell_sort(numeros.copy(), n_acoes[vencedor])

elif vencedor == "Rivaldo":
    bubble_sort(numeros.copy(), n_acoes[vencedor])
    selection_sort(numeros.copy(), n_acoes[vencedor])
    insertion_sort(numeros.copy(), n_acoes[vencedor])

elif vencedor == "Toninho":
    bubble_sort(numeros.copy(), n_acoes[vencedor])
    selection_sort(numeros.copy(), n_acoes[vencedor])
    insertion_sort(numeros.copy(), n_acoes[vencedor])
    shell_sort(numeros.copy(), n_acoes[vencedor])