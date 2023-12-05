import random
def exibirMenu() :
    print("-------------------------------")
    print("1. Embarcar em uma Nova Missão")
    print("2. Explorar o último desafio")
    print("3. Abandonar a Convenção (Sair)")
    print("-------------------------------")

exibirMenu()
entrada = input("Pressione 1, 2 ou digite sair: ")
tentativas = 0

while entrada != "sair":
    if entrada == "1":
        nome = input("Digite seu nome: ")
        num_aleatorio = random.randrange(1,3)
        print(num_aleatorio)
        palpite = int(input(("Adivinhe o código selecionado nas estrelas (1 a 100): ")))
        tentativas += 1

        if palpite == num_aleatorio:
            print(f"Parabéns! Sua vitória foi celebrada em todas as dimensôes conhecidas! Número de tentativas : {tentativas}")
            exibirMenu()
            entrada = input("Pressione 1, 2 ou digite sair: ")
        elif palpite < num_aleatorio:
            print("O código transmitido está em uma galáxia distante em relação ao número secreto...")
        elif palpite > num_aleatorio:
            print("O número transmitido está em uma órbita mais elevada em relação ao número secreto...")

    elif entrada == "2":
        print("Registro do último jogo: ")
        print()
        print(f"A) Nome do jogador(a): {nome}")
        print(f"B) Número de tentativas: {tentativas}")
        print()
        exibirMenu()
        entrada = input("Pressione 1, 2 ou digite sair: ")
    else:
        exibirMenu()
