#**D02** — Leia dois números e exiba o maior. Se forem iguais, informe isso.

numero1= int (input("digite um numero:"))
numero2= int (input("digite outro numero:"))

if numero1 > numero2:
    print(f"O maior é o numero {numero1}")
elif numero2 > numero1:
    print(f"O maior é o numero {numero2}")
    
else:
    print("Os numeros são iguais")
