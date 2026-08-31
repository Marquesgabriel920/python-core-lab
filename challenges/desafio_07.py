# Desafio 07 — tratamento de erro na leitura do JSON
#
# O programa deve:
# - tentar abrir o arquivo data/agendamentos.json;
# - carregar os dados com json.load();
# - informar quantos agendamentos foram lidos;
# - tratar o erro FileNotFoundError;
# - exibir uma mensagem amigável caso o arquivo não exista.

import json

try:
    with open("data/agendamentos.json", "r", encoding="utf-8") as arquivo:
        agendamentos = json.load(arquivo)
    print(f"Arquivo lido com sucesso: {len(agendamentos)} agendamentos.")
    
except FileNotFoundError:
    print("O arquivo de agendamentos não foi encontrado.")
    

