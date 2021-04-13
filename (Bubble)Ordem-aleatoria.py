import random
import timeit

tamanho = int(input('Digite o tamanho: '))

a1 = [0] * tamanho
for i in range(tamanho):
    a1[i] = random.randint(1, 140)

print(f'Lista inicial: {a1}')

def Bubble(a, n: int):
    inicio = timeit.default_timer()
    for j in range(n - 1):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                aux = a[i]
                a[i] = a[i + 1]
                a[i + 1] = aux
    fim = timeit.default_timer()
    print(f'Lista final: {a}')
    print(('%f' % (fim - inicio)))

Bubble(a1, tamanho)