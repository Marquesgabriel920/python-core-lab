#Use a mesma lista de agendamentos do exercicio anterior e crie, usando dictionary comprehensions:

#um dicionário servicos_por_cliente, relacionando cliente e serviço;
#um dicionário valores_por_cliente, relacionando cliente e valor;
#inclua apenas agendamentos com status "Confirmado";
#exiba os dois dicionários.

#Não use for tradicional. Envie o código e o resultado.

agendamentos = [
    {"cliente": "Gabriel", "servico": "corte", "status": "Confirmado", "valor": 40.0},
    {"cliente": "João", "servico": "barba","status": "Confirmado", "valor": 25.0},
    {"cliente": "Marcos", "servico": "sombracelha","status": "Cancelado", "valor": 15.0},
]

servicos_por_cliente= { agendamento["cliente"]: agendamento["servico"] for agendamento in agendamentos if agendamento["status"] == "Confirmado" }

valores_por_cliente= {agendamento["cliente"]: agendamento["valor"] for agendamento in agendamentos if agendamento ["status"]== "Confirmado"}



print (servicos_por_cliente)
print (valores_por_cliente)