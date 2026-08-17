#*D08** — Exiba os primeiros N termos da sequência de Fibonacci, onde N é digitado pelo usuário.

numero=int(input("Digite o número de termos da sequência de Fibonacci que deseja exibir: "))
n1, n2 = 0, 1
count = 0

if numero <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print("Sequência de Fibonacci:")

while count < numero: 
    print(n1, end=' ')
    nth = n1 + n2
    n1 = n2
    n2 = nth 
    count += 1

