import random

print('''
========================
| - Qual o Banco:      |
|  1 - Master Card     |
|  2 - America Express |
|  3 - Diners Club     |
========================
''', end="") 
try:
    Bank = int(input("---> "))
    if Bank == 1:
        firstNumberCard = ['5']
        firstNumberCard.append(str(random.randrange(1, 5)))
        
        NumberCard = firstNumberCard

        for i in range(0, 13):
            NumberCard.append(str(random.randrange(0, 9)))

        finalNumber = []
        finalNumber.extend(NumberCard)

        for i in range(0, len(NumberCard), 2):
            NumberCard[i] = list(str(int(NumberCard[i]) * 2))

        ListNumberCard = []
        for i in NumberCard:
            ListNumberCard.extend(i)

        sumNumbers = 0
        for i in range(0, len(ListNumberCard)):
            sumNumbers += int(ListNumberCard[i]) 
        
        sumNumbers = list(str(sumNumbers))

        digitVerify = []
        digitVerify = list(str(100 - int(sumNumbers[0] + sumNumbers[1])))
        finalNumber.extend(digitVerify[1])
        print(' '.join(finalNumber).replace(" ", ""))
   
        input('Pressione <Enter> para Encerrar!!')
       
except:
    print('Você não digitou um numero, correspondente a um Banco!!')

    