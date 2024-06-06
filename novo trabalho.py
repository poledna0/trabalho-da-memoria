import random

def quadrante(dificul):

    quadrante = [[0 for _ in range()] for _ in range(dificul)]

    for i in range(dificul):
        for j in range(dificul):
            quadrante[i][j] = random.randint(1, 100) 

def ler_entrada():
    vetor = []
    for _ in range(2):
        linha_entrada = int(input('Digite uma linha: '))
        coluna_entrada = int(input('Digite uma coluna: '))
        vetor.append(linha_entrada)
        vetor.append(coluna_entrada)
    return vetor



if __name__ == "__main__":
    escolhendo_a_dificulade = int(input('Digite a dificulade: facil-1, medio-2, dificil-3'))
    if escolhendo_a_dificulade == 1:
        dificul_escolhida = 4

    elif escolhendo_a_dificulade == 2:
        dificul_escolhida = 6

    else:
        dificul_escolhida = 8
    quadrante = [list(range(dificul_escolhida))for _ in range(dificul_escolhida)]
# cmc do cod        
    while True:
        ler_entrada()

