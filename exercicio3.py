pontuacoes_personagens = [[2, 10, 6], [5, 8, 10], [2,4, 6]] # cada vetor é um atributo diferente
soma = 0

for i in range (0, len(pontuacoes_personagens)):
    for j in range (0, len(pontuacoes_personagens[0])):
        soma += pontuacoes_personagens[i][j]

    media = soma / len(pontuacoes_personagens[0])
    print(f"Média do atributo [{i}] : {media}")
    soma = 0



