- CRESCENTE:

import random
import timeit

tamanho = int(input('Digite o tamanho: '))

a1 = [0] * tamanho
for i in range(tamanho):
    a1[i] = random.randint(1, 140)

print(f'Lista inicial: {sorted(a1, key=int)}')

def insertion(a, n: int):
    inicio = timeit.default_timer()
    for j in range(2, n):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    fim = timeit.default_timer()
    print(f'Lista final: {a}')

    print(('%f' % (fim - inicio)))


insertion(sorted(a1, key=int), tamanho)

-----------------------------------------------------------------

- DECRESCENTE:

import random
import timeit

tamanho = int(input('Digite o tamanho: '))

a1 = [0] * tamanho
for i in range(tamanho):
    a1[i] = random.randint(1, 140)

print(f'Lista inicial: {sorted(a1, key=int, reverse=True)}')

def insertion(a, n: int):
    inicio = timeit.default_timer()
    for j in range(2, n):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    fim = timeit.default_timer()
    print(f'Lista final: {a}')

    print(('%f' % (fim - inicio)))


insertion(sorted(a1, key=int, reverse=True), tamanho)

--------------------------------------------------------------------