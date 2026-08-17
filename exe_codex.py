print("Digite suas três notas para saber a média e se foi aprovado ou reprovado")
n1= float(input("Digite a primeira nota"))
n2=  float(input("Digite a segunda nota"))
n3=  float(input("Digite a terceira nota"))
media= (n1+n2+n3)/3
if media >= 7:
    print (f"Parabens sua média foi {media} e você esta aprovado")
else :
     print(f"Sua média foi {media}, infelizmente você esta reprovado.")