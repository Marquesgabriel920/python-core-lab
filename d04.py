#**D04** — Exiba todos os números de 1 a 100 que sejam divisíveis por 3 ou por 5, mas não pelos dois ao mesmo tempo.

# numeros = list(range(1,101)) - deixei essa pra lembrar do começo, criei a lista e depois aprendi que dava para iterar no range sem precisar da lista, como esta abaixo.

for numero in range( 0,101):
    if (numero % 3 == 0) != (numero % 5 == 0):
        print(numero)
        