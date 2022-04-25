cpf = input('Digite um CPF: ').replace("-", "")
cpfBase1 = list(cpf[:11].replace(".", ""))
cpfBase2 = list(cpf[:12].replace(".", ""))

multSepCpf = [0]*9
numberMultCpf1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
numberMultCpf2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

# Primeiro Digito Verificador
for i in range(0, 9):
    multSepCpf[i] = int(cpfBase1[i]) * numberMultCpf1[i]

somaNumberList = 0

for i in multSepCpf:
    somaNumberList += i

somaNumberList = somaNumberList % 11

digitVerify1 = 0

if somaNumberList == 0 or somaNumberList == 1:
    digitVerify1 = 0
else:
    digitVerify1 = 11 - somaNumberList

# Segundo Digito Verificador
multSepCpf = [0]*10

for i in range(0, 10):
    multSepCpf[i] = int(cpfBase2[i]) * numberMultCpf2[i]

somaNumberList = 0

for i in multSepCpf:
    somaNumberList += i

somaNumberList = somaNumberList % 11

digitVerify2 = 0

if somaNumberList == 0 or somaNumberList == 1:
    digitVerify2 = 0
else:
    digitVerify2 = 11 - somaNumberList

# Mensagem de Validação
if digitVerify1 == int(cpf[11]) and digitVerify2 == int(cpf[12]):
    print(f'Este CPF: {cpf[:11]}-{cpf[11:]} é válido')
else:
    print(f'Este CPF: {cpf} é inválido')

# para verificar o estado de emissão =>>>    cpf[10]





