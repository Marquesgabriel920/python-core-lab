#**D05** — Crie um jogo de adivinhar: o programa sorteia um número de 1 a 10 e o usuário tem 3 tentativas para acertar. Informe se errou pra cima ou pra baixo.

import random 

sorteio= random.randint(1,10)
contador= 0

while contador < 3:
    tentativa= int(input("Chute um numero de 1 a 10:"))
    if sorteio < tentativa:
        print("Errou para cima")
    elif sorteio > tentativa:
        print("Errou para baixo")
    else:
        print("Você acertou o numero!")
        if sorteio== tentativa:
            break
        
    contador += 1
    if contador >=3 :
        print("Infelizmente nao acertou em 3 tentativs!")
    