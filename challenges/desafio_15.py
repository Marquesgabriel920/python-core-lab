#Crie esta lista:

#Use list comprehensions para criar:

#uma lista com os nomes dos clientes confirmados;
#uma lista com os valores dos agendamentos confirmados;
#uma lista com os nomes dos clientes em letras maiúsculas.

#Depois, exiba as três listas.

agendamentos = [
    {"cliente": "Gabriel", "status": "Confirmado", "valor": 40.0},
    {"cliente": "João", "status": "Confirmado", "valor": 25.0},
    {"cliente": "Marcos", "status": "Cancelado", "valor": 15.0},
]

clientes_confirmados= [agendamento["cliente"] for agendamento in agendamentos if agendamento["status"]== "Confirmado"]

valores_agendamentos_confirmados= [agendamento["valor"] for agendamento in agendamentos if agendamento["status"]== "Confirmado"]

clientes_confirmados_maiuscula= [agendamento["cliente"].upper() for agendamento in agendamentos if agendamento["status"]== "Confirmado"]

print(clientes_confirmados)
print(valores_agendamentos_confirmados)
print(clientes_confirmados_maiuscula)