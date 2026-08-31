# Crie um programa que:

#solicite serviços separados por vírgula;
#use .split(",");
#remova espaços extras com .strip();
#formate os serviços com .title();
#remova serviços duplicados usando set;
#mostre os serviços únicos e a quantidade.

servicos= input(" Digite os serviços separados por virgulas:")

servicos_separados= servicos.split(",")

servicos_tratados= []

for servico in servicos_separados:
    servico_limpo= servico.strip().title()
    servicos_tratados.append(servico_limpo)
    
servicos_unicos= set(servicos_tratados)

print(f" Serviços: {servicos_unicos}, quantidade: {(len(servicos_unicos))}")