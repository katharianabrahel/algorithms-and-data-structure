#'contador' começa em 0 já que inicia-se com as pessoas sozinhas

def grupos(n, subgrupo=[], contador=0):
    if contador == n: #condição para printar o subgrupo
        print(subgrupo)
        return
    for i in range(1, n + 1 - contador):
        if subgrupo and i < subgrupo[-1]:
            #evita repetições do mesmo subgrupo com os mesmos valores mas em ordem diferente
            continue 
        grupos(n, subgrupo + [i], contador + i)


n = int(input())
print(f'Uma sessão com {n} pessoas pode ter sua audiência nos seguintes subgrupos:')
grupos(n)