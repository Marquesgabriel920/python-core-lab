import json

with open("data/agendamentos.json", "r", encoding="utf-8") as arquivo:
    agendamentos = json.load(arquivo)
    

novo_agendamento = {
    "cliente": "Ana",
    "serviço": "Corte",
    "status": "Confirmado",
    "valor": 30.00
}

agendamentos.append(novo_agendamento)

with open("data/agendamentos.json", "w", encoding="utf-8") as arquivo:
    json.dump(agendamentos, arquivo, ensure_ascii=False, indent=4)