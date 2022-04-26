NumberCard = input('Digite o Numero do Cartão: ')
NumberCard = list(NumberCard.replace(" ", ""))

def ValidarCard():
    for i in range(len(NumberCard)-2, -1, -2):
        NumberCard[i] = list(str(int(NumberCard[i]) * 2))

    ListNumberCard = []
    for i in NumberCard:
        ListNumberCard.extend(i)

    sumNumbers = 0
    for i in range(0, len(ListNumberCard)-1):
        sumNumbers += int(ListNumberCard[i]) 

    Result = (sumNumbers + int(NumberCard[len(NumberCard)-1])) % 10
    return Result

try:
    
    for i in range(0, len(NumberCard)-1):
        NotCaractere = int(NumberCard[i])

    if len(NumberCard) >= 13 and len(NumberCard) <= 16:   
        # MasterCard
        if int(NumberCard[0] + NumberCard[1]) >= 51 and int(NumberCard[0] + NumberCard[1]) <= 55:

            Result = ValidarCard()
                    
            if Result == 0:
                print("Cartão MASTER CARD Válido!!")
            else:
                print("Cartão MASTER CARD Invalido!!")
                
        # Visa
        elif int(NumberCard[0]) == 4:
            
            Result = ValidarCard()
                    
            if Result == 0:
                print("Cartão Visa Válido!!")
            else:
                print("Cartão Visa Invalido!!")
        # Amex
        elif int(NumberCard[0] + NumberCard[1]) == 34 or int(NumberCard[0] + NumberCard[1]) == 37:
            
            Result = ValidarCard()

            if Result == 0:
                print("Cartão America Express Válido!!")
            else:
                print("Cartão America Express Invalido!!")       
        # Diners
        elif int(NumberCard[0] + NumberCard[1]) == 30 or int(NumberCard[0] + NumberCard[1]) == 36 or int(NumberCard[0] + NumberCard[1]) == 38:
            Result = ValidarCard()

            if Result == 0:
                print("Cartão Diners Válido!!")
            else:
                print("Cartão Diners Invalido!!")  
        # Discover
        elif int(NumberCard[0] + NumberCard[1] + NumberCard[2]) == 6011:
            Result = ValidarCard()

            if Result == 0:
                print("Cartão Discover Válido!!")
            else:
                print("Cartão Discover Invalido!!")  
        else: 
            print("Este Cartão não Está na nossa DB, só validamos Cartões com as seguintes bandeiras"
             + "(MasterCard, Discover,  Diners, America Express, Visa)")
    else:
        print('Quantidade de Numeros Inválidos!!')

except:
    print('O Numero do cartão não corresponde a uma sequência de caracteres' 
    + ' válidos(Contém letras, caracteres especiais ou não se relacionam a uma bandeira especifica)!!')


