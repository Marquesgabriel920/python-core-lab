#Crie uma função calcular_valor_final que:

#receba o valor de um serviço;
#receba um percentual de desconto;
#calcule o valor final;
#retorne o resultado.

#Fora da função:

#solicite os valores com input();
#faça as conversões;
#chame a função;
#exiba o valor final

def calcular_valor_final(valor, desconto):
    valor_desconto= valor * (desconto/100)
    total= valor - valor_desconto
    
    return total


if __name__ == "__main__":  
    valor=float(input("Digite o valor do produto:"))
    desconto=float(input("Digite o percentual de desconto:"))

    valor_final=calcular_valor_final(valor, desconto)

    print(f"O valor a pagar com desconto é {valor_final}")

