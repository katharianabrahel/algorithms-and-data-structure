def checkar_entrada(string):
    #lista criada para armazenar a posição dos F
    indice = []
    for i in range(len(string)):
        if string[i] == 'F':
            #adiciona a posição dos Fs
            indice.append(i+1)
        elif string[i] == 'V':
            #confere se existe F que correspode ao V
            if len(indice) == 0:
                return f"Incorreto, devido a capa na posição {i+1}."
            else:
            #remove o F da primeira posição da lista
                indice.pop(0)
    #se no fim a lista estiver vazia, significa que todos os Fs possuem um V correspondente
    if len(indice) == 0:
        return "Correto."
    else:
        return f"Incorreto, devido a capa na posição {indice[0]}."
    
entrada = input()
print(checkar_entrada(entrada))