#**D09** — Crie uma lista com 5 números digitados pelo usuário. Exiba o maior, o menor e a média entre os dois.


numeros = input("Digite 5 números separados por espaço: ").split()


for numero in numeros:
    
    maior=numeros[0]
    if int(numero) > int(maior):
        maior=numero
    else: continue
   

for numero in numeros:
        menor=numeros[0]
        if int (numero) < int(menor):
            menor= numero
        else: continue
        
print(f"O maior número é {maior}, o menor é {menor} e a média é {(int(maior)+int(menor))/2}")
