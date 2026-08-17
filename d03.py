#**D03** — Leia 3 notas de um aluno e calcule a média. Exiba se foi aprovado (≥7), em recuperação (≥5 e <7) ou reprovado (<5).

nota1= float (input("Digite a primeira nota:"))
nota2= float (input("Digite a segunda nota:"))
nota3= float (input("Digite a terceira nota:"))

media= (nota1 + nota2 +nota3)/3

if media >= 7:
    print("Parabens você esta aprovado!")
elif media >=5 and media <7:
    print("Você esta em recuperação!")
else:
    print("Você esta reprovado!")

