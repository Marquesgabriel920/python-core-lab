import json

try:
    with open("data/agendamentos.json", "r", encoding="utf-8") as arquivo:
        agendamentos = json.load(arquivo)
    print(f"Arquivo lido com sucesso: {len(agendamentos)} agendamentos.")
    
except FileNotFoundError:
    print("O arquivo de agendamentos não foi encontrado.")
    

