def heapify_max(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2
	if l < n and arr[i] < arr[l]:
		largest = l
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])
		heapify_max(arr, n, largest)

def heapify_min(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)

#função pra achar o valor máximo usando heap max
def max_value(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify_max(lista, n, i)

#função pra achar o valor minimo usando heap min
def min_value(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(lista, n, i)


numeros = list(map(int, input().split()))
constante = int(input())
rodadas = 0

while len(numeros) > 0:
	min_value(numeros)
    #apos fazer heap min, o menor valor será o primeiro elemento
	minimo = numeros[0]
    #apos fazer heap max, o maior valor será o primeiro elemento
	max_value(numeros)
	maximo = numeros[0]
	k = maximo - abs(minimo * constante)
	numeros.remove(maximo)
	if k > 0:
		numeros.append(k)
	rodadas += 1
	
print(f"{rodadas} rodadas, partindo para a próxima!")