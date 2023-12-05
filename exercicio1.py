cartas = []
numeroCartas = int(input("Digite o número de cartas: "))

for i in range (0, numeroCartas):
    carta = int(input("Digite o valor de cada carta: "))
    cartas.append(carta)


for i in range (0, numeroCartas):
    cartaValiosa = ""

    for j in range (1, numeroCartas):
        if cartas[j] > cartas[i]:
            cartaValiosa = cartas[j]

    if cartaValiosa == "":
        cartaValiosa = cartas[i]

print(f"Valores das suas cartas: {cartas}")
print(f"Carta mais valiosa: {cartaValiosa}")
