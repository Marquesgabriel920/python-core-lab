#Crie uma lista - O programa deve:

#solicitar um nome;
#remover espaços extras da busca;
#ignorar diferenças entre maiúsculas e minúsculas;
#percorrer a lista;
#exibir o nome original se encontrar;
#informar caso não encontre.

clientes = ["Gabriel Marques", "João Silva", "Marcos Souza"]

nome_buscado= input("Digite seu nome:")

nome_buscado_tratado= nome_buscado.strip().casefold()
encontrado=False
for cliente in clientes:
    if cliente.casefold() == nome_buscado_tratado:
        encontrado= True
        print(f"Nome {cliente} encontrado na lista.")
        break

    
else:
        print("Nome não encontrado na lista")
        