from challenges.desafio_18 import calcular_valor_final


resultado_teste_1 = calcular_valor_final(100, 10)
assert resultado_teste_1 == 90.0

print("Teste 1 aprovado")

resultado_teste_2 = calcular_valor_final(200, 10)

assert resultado_teste_2 == 180.0


print("Teste 2 aprovado")

resultado_teste_3 = calcular_valor_final(50, 0)

assert resultado_teste_3 == 50.0


print("Teste 3 aprovado")

resultado_teste_4 = calcular_valor_final(80, 25)

assert resultado_teste_4 == 60.0


print("Teste 4 aprovado")

resultado_teste_5 = calcular_valor_final(100, 100)

assert resultado_teste_5 == 0.0


print("Teste 5 aprovado")

resultado_teste_6 = calcular_valor_final(100, 7.5)

assert resultado_teste_6 == 92.5


print("Teste 6 aprovado")

resultado_teste_7 = calcular_valor_final(120, 5)

assert resultado_teste_7 == 114.0


print("Teste 7 aprovado")

resultado_teste_8 = calcular_valor_final(300, 30)

assert resultado_teste_8 == 210.0

print("Teste 8 aprovado")