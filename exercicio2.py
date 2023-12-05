pontuacoes = []
pontuacao = 1
soma = 0

pontuacao = float(input("Entre com suas maiores pontuações, ao término digite 0: "))

while pontuacao != 0:
    pontuacoes.append(pontuacao)
    pontuacao = float(input("Entre com suas maiores pontuações, ao término digite 0: "))


for i in range (0, len(pontuacoes)):
    soma += pontuacoes[i]

media = soma / len(pontuacoes)

print(f"Média de pontuações: {media}")