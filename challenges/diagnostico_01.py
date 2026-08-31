#Exercício:

#Leia 5 números inteiros em uma única entrada.
#Mostre o maior número.
#Mostre o menor número.
#Mostre a soma.
#Mostre a média.
#Não use max(), min() ou sum().
#O programa deve funcionar também com números negativos.


numeros = [int(x) for x in input("Digite cinco números inteiros separados por espaço: ").split()]

maior=numeros[0]
menor=numeros[0]
soma=0


for numero in numeros:
    soma+=numero
    
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    
    

media = soma/ len(numeros)

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print(f"A soma é {soma}")
print(f"A média é {media}")
    


