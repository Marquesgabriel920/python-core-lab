# Desafio 04 — busca linear
#
# Utilize uma lista de números inteiros.
#
# O programa deve:
# - solicitar um número ao usuário;
# - percorrer a lista usando for;
# - informar se o número foi encontrado;
# - contar a quantidade de comparações realizadas;
# - exibir essa quantidade ao final.
#
# A complexidade do algoritmo deve ser O(n).


numeros=[1,15,6,9,7,3,4,11,19,65,48,2,18,55]

numdigitado=int(input("Digite um numero inteiro:"))

diferente=0
igual=0
for numero in numeros:
    if numero != numdigitado:
        diferente+=1
    else:
        igual+=1
        print(f"O numero {numdigitado} foi encontrado na lista.")

comparações= (igual+diferente)

print(f"A quantidade de comparações realizada foi {comparações}")