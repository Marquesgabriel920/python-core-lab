# Desafio 06 — adicionar agendamento no arquivo JSON
#
# O programa deve:
# - ler os agendamentos do arquivo data/agendamentos.json;
# - criar um novo agendamento;
# - adicionar o novo agendamento à lista;
# - salvar a lista atualizada no arquivo JSON;
# - preservar a formatação e a acentuação dos dados.



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