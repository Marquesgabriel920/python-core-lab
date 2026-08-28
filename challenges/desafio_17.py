#Usando a mesma lista de agendamentos do exercicio anterior, crie um set chamado servicos_confirmados que:

#contenha apenas serviços de agendamentos confirmados;
#elimine serviços repetidos;
#formate os nomes com .title();
#seja criado usando set comprehension;
#seja exibido junto com sua quantidade.

#Não use for tradicional.

agendamentos = [
    {"cliente": "Gabriel", "servico": "corte", "status": "Confirmado", "valor": 40.0},
    {"cliente": "João", "servico": "barba","status": "Confirmado", "valor": 25.0},
    {"cliente": "Paulo", "servico": "luzes","status": "Confirmado", "valor": 150.0},
    {"cliente": "Pedro", "servico": "barba","status": "Cancelado", "valor": 25.0},
    {"cliente": "Thiago", "servico": "barba","status": "Confirmado", "valor": 25.0},
    {"cliente": "Marcos", "servico": "sombracelha","status": "Cancelado", "valor": 15.0},
]

servicos_confirmados={agendamento["servico"].title() for agendamento in agendamentos if agendamento["status"]== "Confirmado"}


print(f"os serviços confirmados são {servicos_confirmados}, quantidade {len(servicos_confirmados)}")