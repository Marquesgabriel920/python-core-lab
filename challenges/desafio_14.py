#Refatore o exercício anterior:

#crie uma função chamada normalizar_telefone;
#faça a função receber o telefone;
#remova parênteses, espaços e hífen dentro dela;
#retorne o telefone limpo;
#solicite o telefone fora da função;
#chame a função;
#valide se o resultado possui 11 dígitos.

#A função deve cuidar apenas da limpeza. A entrada, as mensagens e a validação devem ficar fora dela.

def normalizar_telefone(telefone):
    telefone_limpo = telefone.replace("(", "")
    telefone_limpo = telefone_limpo.replace(")", "")
    telefone_limpo = telefone_limpo.replace("-", "")
    telefone_limpo = telefone_limpo.replace(" ", "")
    return telefone_limpo

telefone=(input("Digite um telefone neste formato (xx) xxxx-xxxx :"))

telefone_normalizado= normalizar_telefone(telefone)

if len(telefone_normalizado)== 11:
    print ("Telefone Válido")
else: 
    print ("Telefone invalido")