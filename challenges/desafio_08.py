#crie uma lista com serviços repetidos;
#converta essa lista para um set;
#imprima o conjunto;
#verifique se "Corte" está presente;
#exiba a quantidade de serviços únicos.

servicos = [
    "Corte",
    "Barba",
    "Corte",
    "Sobrancelha",
    "Barba",
    "Corte"
]

servicos_unicos= set(servicos)

print (servicos_unicos)

if "Corte" in  servicos_unicos:
    print("O serviço de corte está disponível.")
    
print(f"A quantidade de serviços disponiveis é {len(servicos_unicos)}")