matriz_portal = []
linhas = int(input("Digite a quantidade de linhas da sua matriz: "))
colunas = int(input("Digite a quantidade de colunas da sua matriz: "))
identidade = False

for i in range (0, linhas):
    matriz_portal.append([])
    for j in range (0, colunas):
        matriz_portal[i].append(int(input(f"Digite apenas valores binários para matriz_portal[{i}][{j}]: ")))

for i in range (0, linhas):
    if matriz_portal[i][i] != 1:
        identidade = False
    else:
        identidade = True


if identidade:
    print("Parabéns!! Sua matriz atende os critérios da  Matriz Identidade Intergaláctica")
else:
    print("Sua matriz não é uma matriz identidade, portanto, não atende os critérios da  Matriz Identidade Intergaláctica...")



