
agendamentos= [
    {"cliente": "Gabriel", "serviço": "Corte", "status": "Confirmado", "valor": 40.00},
    {"cliente": "Joao", "serviço": "Barba", "status": "Confirmado", "valor": 25.00},
    {"cliente": "Marcos", "serviço": "Sombracelha", "status": "Cancelado", "valor": 15.00},
    {"cliente": "Maria", "serviço": "Hidratação", "status": "Cancelado", "valor": 90.00},
]
encontrado=False
cliente_buscado = input("Digite o nome do cliente: ")
for agendamento in agendamentos:
    if agendamento["cliente"]== cliente_buscado:
        encontrado=True
        print(agendamento["cliente"],agendamento["serviço"],agendamento["status"],agendamento["valor"])
    
if not encontrado:
    print("“Cliente não encontrado”")

contador=0
total=0
for agendamento in agendamentos:
    print(agendamento["cliente"],agendamento["serviço"])
for agendamento in agendamentos:
        if agendamento["status"] == "Confirmado":
            contador+=1
            total= total+ agendamento["valor"]
            print(agendamento["cliente"], agendamento["status"])

print(f"A quantidade de agendamentos confirmados é {contador}")
print(f"O valor total dos agendamentos é de {total}")        
        
    
