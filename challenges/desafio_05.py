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