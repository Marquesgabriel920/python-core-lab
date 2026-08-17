#**D01** — Leia um número e diga se é par ou ímpar *

outro = "S"

while outro == "S":
    numero = int(input("digite um numero:"))
    
    if numero % 2 == 0:
        print("par")
    else:
        print("impar")
    
    outro = input("Deseja saber outro numero? S/N")