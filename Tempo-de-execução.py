import numpy as np
import timeit
import random

exemplo2 = float()
exemplo3 = float()
exemplo4 = float()
continuar = 'sim'


def tipo_dimensional(dimensao):
    if dimensao == 'vetor':
        tamanho = int(input('Digite o tamanho do vetor: '))

        vetor1 = [0] * tamanho
        vetor2 = [0] * tamanho
        res = [0] * tamanho

        inicio = timeit.default_timer()

        for i in range(tamanho):
            vetor1[i] = random.randint(1, 15)
            vetor2[i] = random.randint(16, 30)

            res[i] = vetor1[i] + vetor2[i]

        fim = timeit.default_timer()

        global exemplo2
        exemplo2 = ('%f' % (fim - inicio))

    if dimensao == 'matriz':

        funcao = str(input('Soma ou produto das matrizes: (soma ou produto)'))

        if funcao == 'soma':
            x = int(input('digite a quantidade de linhas: '))
            y = int(input('digite a quantidade de colunas: '))

            matriz1 = [[0] * x] * y
            matriz2 = [[0] * x] * y
            resultado = [[0] * x] * y

            matriz1 = np.random.randint(0, 100, (x, y))
            matriz2 = np.random.randint(0, 100, (x, y))
            resultado = np.random.randint(0, 100, (x, y))

            inicio = timeit.default_timer()
            for l in range(0, x):
                for c in range(0, y):
                    resultado[l][c] = matriz1[l][c] + matriz2[l][c]
            fim = timeit.default_timer()

            global exemplo3
            exemplo3 = ('%f' % (fim - inicio))

        if funcao == 'produto':
            matriz1 = [[0] * 100] * 100
            matriz2 = [[0] * 100] * 100
            produto = [[0] * 100] * 100

            matriz1 = np.random.randint(0, 100, (100, 100))
            matriz2 = np.random.randint(0, 100, (100, 100))
            resultado = np.random.randint(0, 100, (100, 100))

            inicio = timeit.default_timer()
            for i in range(0, 100):
                for j in range(0, 100):
                    produto[i][j] = 0
                    for k in range(0, 100):
                        produto[i][j] = produto[i][j] + matriz1[i][k] * matriz2[k][j]
            fim = timeit.default_timer()

            global exemplo4
            exemplo4 = ('%f' % (fim - inicio))


while continuar == 'sim':
    tipo = str(input('digite qual tipo dimensional: (vetor ou matriz)'))

    tipo_dimensional(tipo)

    print(f'\nExemplo2: {exemplo2}')
    print(f'Exemplo3: {exemplo3}')
    print(f'Exemplo4: {exemplo4}')

    continuar = str(input('Deseja continuar? (sim ou não)'))
