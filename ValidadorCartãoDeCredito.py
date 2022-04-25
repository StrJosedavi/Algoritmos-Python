NumberCard = input('Digite o Numero do Cartão: ')
NumberCard = list(NumberCard.replace(" ", ""))

try:
    
    for i in range(0, len(NumberCard)-1):
        NotCaractere = int(NumberCard[i])

    if len(NumberCard) >= 13 and len(NumberCard) <= 16:
        if len(NumberCard) == 16:
            # MasterCard
            if int(NumberCard[0] + NumberCard[1]) >= 51 and int(NumberCard[0] + NumberCard[1]) <= 55:

                for i in range(1, len(NumberCard), 2):
                    NumberCard[i] = list(str(int(NumberCard[i]) * 2))

                ListNumberCard = []
                for i in NumberCard:
                    ListNumberCard.extend(i)

                sumNumbers = 0
                for i in range(0, len(ListNumberCard)-1):
                    sumNumbers += int(ListNumberCard[i]) 

                Result = sumNumbers % 10
                    
                if Result == 0:
                        print("Cartão MASTER CARD Válido!!")
                else:
                        print("Cartão MASTER CARD Invalido!!")
                
            # Visa
            elif int(NumberCard[0]) == 4:
                print()
            # Amex
            elif int(NumberCard[0] + NumberCard[1]) == 34 or int(NumberCard[0] + NumberCard[1]) == 37:
                print()       
            # Diners
            elif int(NumberCard[0] + NumberCard[1]) == 30 or int(NumberCard[0] + NumberCard[1]) == 36 or int(NumberCard[0] + NumberCard[1]) == 38:
                print()    
            # Discover
            elif int(NumberCard[0] + NumberCard[1] + NumberCard[2]) == 6011:
                print()    
    else:
        print('Quantidade de Numeros Inválidos!!')

except:
    print('O Numero do cartão não corresponde a uma sequência de caracteres' 
    + ' válidos(Contém letras, caracteres especiais ou não se relacionam a uma bandeira especifica)!!')


