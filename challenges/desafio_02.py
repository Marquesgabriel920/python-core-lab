#Desafio 2 — maior e menor número

#O programa deve:

#receber 5 números inteiros;
#usar um for;
#encontrar o maior e o menor número;
#não usar max() nem min().

numeros= [int(x)for x in input("Digite cinco numeros inteiros para saber o maior e o menor:").split()]

maior= numeros[0]
menor= numeros[0]
for numero in numeros:
   if numero > maior:
         maior= numero
   elif numero < menor:
       menor= numero
       
print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}")