#Crie uma função resumir_financas(lancamentos) que:

#receba a lista como parâmetro;
#calcule o total das entradas;
#calcule o total das saídas;
#calcule o saldo;
#retorne um dicionário com esses três resultados;
#não use input() dentro da função;
#não use sum().


lancamentos = [
    {"descricao": "Salário", "tipo": "entrada", "valor": 2500.0},
    {"descricao": "Aluguel", "tipo": "saida", "valor": 900.0},
    {"descricao": "Internet", "tipo": "saida", "valor": 100.0},
    {"descricao": "Freelance", "tipo": "entrada", "valor": 450.0},
    {"descricao": "Transporte", "tipo": "saida", "valor": 50.0},
]

def resumir_financas(lancamentos):
    total_entradas = 0.0
    total_saidas = 0.0

    for lancamento in lancamentos:
        if lancamento["tipo"]== "entrada":
            total_entradas += lancamento["valor"]
        elif lancamento["tipo"]== "saida":
            total_saidas+=lancamento["valor"]

    saldo=(total_entradas -total_saidas)    

    return {
        "total_entradas": total_entradas,
        "total_saidas": total_saidas,
        "saldo": saldo
    }
    
    
resumo = resumir_financas(lancamentos)

assert resumo["total_entradas"] == 2950.0
assert resumo["total_saidas"] == 1050.0
assert resumo["saldo"] == 1900.0

print("Todos os testes foram aprovados")

resumo_vazio = resumir_financas([])

assert resumo_vazio == {
    "total_entradas": 0.0,
    "total_saidas": 0.0,
    "saldo": 0.0
}

print("Teste com lista vazia aprovado")