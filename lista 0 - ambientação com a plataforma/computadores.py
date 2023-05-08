import math

n = int(input())
computador1 = input().split(' - ')
computador2 = input().split(' - ')

complexidade1 = 0.0
complexidade2 = 0.0

if computador1[3] == '2n^2':
    complexidade1 = 2*n**2
elif computador1[3] == 'nlogn':
    complexidade1 = n*math.log(n,10)
elif computador1[3] == '2^n':
    complexidade1 = 2**n
elif computador1[3] == 'n':
    complexidade1 = n

if computador2[3] == '2n^2':
    complexidade2 = 2*n**2
elif computador2[3] == 'n.logn':
    complexidade2 = n*math.log(n,10)
elif computador2[3] == '2^n':
    complexidade2 = 2**n
elif computador2[3] == 'n':
    complexidade2 = n

velocidade1 = complexidade1/int(computador1[1])
print(f'Velocidade do {computador1[0]}: {velocidade1:.2f} segundos')
velocidade2 = complexidade2/int(computador2[1])
print(f'Velocidade do {computador2[0]}: {velocidade2:.2f} segundos')

if velocidade1 < velocidade2:
    print(f'O {computador1[0]} foi mais rápido!')
else:
    print(f'O {computador2[0]} foi mais rápido!')
