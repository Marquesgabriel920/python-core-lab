#Desafio 1 — contagem de pares e ímpares

#O programa deve:

#receber exatamente 5 números inteiros;
#usar uma repetição for;
#calcular a soma;
#contar quantos são pares e quantos são ímpares;
#usar % para verificar a paridade.

numeros=[int(x) for x in input("Digite cinco numeros inteiros separados por espaço: ").split()]
soma=0 
contimpar=0
contipar=0
for numero in numeros:
  
    soma= soma+ numero
    
    if numero % 2 == 0 :
        contipar += 1
    else: 
        contimpar += 1
        
print(f"A soma dos valores passado é {soma}")
print(f"A quantidade de numeros ímpares é {contimpar}")
print(f"A quantidade de numeros pares é {contipar}")