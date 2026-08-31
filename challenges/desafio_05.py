# Desafio 05 — leitura de agendamentos em JSON
#
# O programa deve:
# - ler o arquivo data/agendamentos.json;
# - exibir o cliente e o serviço de cada agendamento;
# - contar os agendamentos confirmados;
# - somar o valor dos agendamentos confirmados;
# - exibir a quantidade e o valor total.



import json

with open("data/agendamentos.json", "r", encoding="utf-8") as arquivo:
    agendamentos = json.load(arquivo)


contador=0
total=0
for agendamento in agendamentos:
    print(agendamento["cliente"], agendamento["serviço"])
    if agendamento ["status"]== "Confirmado":
        contador+=1
        total+= agendamento["valor"]

print(f"O total de agendamentos confirmados é {contador}, somando o valor de {total}")