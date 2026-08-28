# Normalização de nome - O programa deve:

#solicitar o nome de um cliente;
#remover espaços extras;
#verificar se o nome ficou vazio;
#se estiver vazio, exibir uma mensagem de nome inválido;
#caso contrário, exibir:
#o nome original;
#o nome normalizado para busca;
#o nome formatado para apresentação.

nome= input("Digite seu nome:")

nometratado= nome.strip()

if nometratado=="": 
    print('Nome invalido!')
else :
    print(f"Nome original: {nome}")
    print(f"Nome normalizado para busca {(nometratado).casefold()}")
    print(f"Nome formatado para apresentação {(nometratado).title()}")
    

