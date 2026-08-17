#**D06** — Calcule o fatorial de um número digitado pelo usuário usando um loop (sem recursão).

numero=int(input("Digite um numero inteiro e positivo para saber o fatorial:"))
fatorial=1

for i in range(1,numero+1):
    fatorial=fatorial*i
    
print(f"O fatorial de {numero} é {fatorial}")
