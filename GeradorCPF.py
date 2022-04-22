import random

####################################################
#           Gerando Primeiro Digito                #
####################################################

numberAleatório = list(str(random.randrange(100000000, 999999999)))
numBaseForMultDig = [10, 9, 8, 7, 6, 5, 4, 3, 2]

multAllDig = [0]*9

for i in range(0, 9):
    multAllDig[i] = int(numberAleatório[i]) * numBaseForMultDig[i] 

resultMultDig = 0

for i in multAllDig:
    resultMultDig += i

resultMultDig = resultMultDig % 11

firstDig = 0
if resultMultDig == 0 or resultMultDig == 1:
    firstDig = 0
else:
    firstDig = 11 - resultMultDig

numberAleatório.append(str(firstDig))

####################################################
#           Gerando Segundo Digito                #
####################################################

numBaseForMultDig = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
multAllDig = [0]*10

for i in range(0, 10):
    multAllDig[i] = int(numberAleatório[i]) * numBaseForMultDig[i] 

resultMultDig = 0

for i in multAllDig:
    resultMultDig += i

resultMultDig = resultMultDig % 11

SecondDig = 0
if resultMultDig == 0 or resultMultDig == 1:
    SecondDig = 0
else:
    SecondDig = 11 - resultMultDig

numberAleatório.append(str(SecondDig))

####################################################

cpf = (numberAleatório[0:3], numberAleatório[3:6], numberAleatório[6:9], numberAleatório[9:12])
cpfFormat = "".join(cpf[0]) + "." + "".join(cpf[1]) + "." +"".join(cpf[2]) + "-" + "".join(cpf[3])

print(cpfFormat)
input("Pressione <enter> para encerrar!")

