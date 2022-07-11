def conta_bomba(A, lin, col):
 posicoes_com_bomba = 0
 if lin > 0 and A[lin-1][col] == -1:
    posicoes_com_bomba += 1
 if lin < len(A) - 1 and A[lin+1][col] == -1:
    posicoes_com_bomba += 1
 if col > 0 and A[lin][col-1] == -1:
    posicoes_com_bomba += 1
 if col < len(A[0]) - 1 and A[lin][col+1] == -1:
    posicoes_com_bomba += 1
 return posicoes_com_bomba
 