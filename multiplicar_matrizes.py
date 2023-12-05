def matrizesMult(matriz1, matriz2):
    linhas_matriz1 = len(matriz1)
    colunas_matriz1 = len(matriz1[0])
    linhas_matriz2 = len(matriz2)
    colunas_matriz2 = len(matriz2[0])

    if colunas_matriz1 != linhas_matriz2:
        print("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")

    resultado = [[0 for i in range(colunas_matriz2)] for j in range(linhas_matriz1)]

    for i in range(linhas_matriz1):
        for j in range(colunas_matriz2):
            for k in range(colunas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado


matriz_a = [[4, 6, 9], [0, 0, 0]]
matriz_b = [[6, 9], [1, 2], [0,0]]

resultado = matrizesMult(matriz_a, matriz_b)
print(resultado)