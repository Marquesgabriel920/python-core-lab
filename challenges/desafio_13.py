#Crie um programa que:

#solicite um telefone;
#preserve o telefone original;
#remova parênteses, espaços e hífen;
#mostre o telefone original;
#mostre o telefone normalizado;
#verifique se o telefone possui 11 dígitos.

telefone=(input("Digite um telefone neste formato (xx) xxxx-xxxx :"))

telefone_limpo= telefone.replace("(","").replace(")","").replace("-","").replace(" ", "")

print(f"Telefone Original {telefone}")
print(f"Telefone Normalizado {telefone_limpo}")
if len(telefone_limpo) == 11:
    print (f"Telefone Válido")
else:
    print("Telefone invalido")