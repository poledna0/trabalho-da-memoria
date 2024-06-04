import time
numeros_que_ja_acertou = []
contagem_de_socorro = 0
quadrante = [['a', 'b', 'c', 'd'],
              ['a', 'b', 'c', 'd'],
              ['e', 'f', 'g', 'h'],
              ['e', 'f', 'g', 'h']]

def mostra_quadrante(matriz):
    for linha in matriz:
        print('-'.join(linha))
        print('-------')

def censura_verifica_acertos_tb (vetor):# fututamente add numeros que ja acertou, ja declarado no inicio do cod
    vetor_censurado = [list(range(4)) for _ in range(4)]
    for linha in range(len(vetor)):
        for coluna in range(len(vetor)):
            vetor_censurado[linha][coluna] = '#'
    for linha in vetor_censurado:
        print('-'.join(linha))
        print('-------')
    return vetor_censurado

def ler_entrada():
    vetor = []
    for _ in range(2):
        linha_entrada = int(input('Digite uma linha: '))
        coluna_entrada = int(input('Digite uma coluna: '))
        vetor.append(linha_entrada)
        vetor.append(coluna_entrada)
    return vetor

def socorro (vetor, contador):
    entrada = input("Você precisa de ajuda? S/n: ")
    print('\033c', end='')
    if entrada == 'S' or entrada == 's':
        mostra_quadrante(vetor)
        contador += 1
        time.sleep(3)
        print('\033c', end='')
    return contador


if __name__ == "__main__":
    mostra_quadrante(quadrante)
    # tempo para ocultar as respectivas respostas.
    time.sleep(1)
    print('\033c', end='')

    while True:
        # pega o vetor com as posições
        vetor_da_entrada = ler_entrada()
        if quadrante[vetor_da_entrada[0]][vetor_da_entrada[1]] == quadrante[vetor_da_entrada[2]][vetor_da_entrada[3]]:
            print('Você acertou, parabéns amigue')# mostrar se ele acertou 
        censura_verifica_acertos_tb(quadrante)# fututamente add numeros que ja acertou, ja declarado no inicio do cod
        if contagem_de_socorro < 3:
            socorro(quadrante, contagem_de_socorro)
            print(contagem_de_socorro)
        else:
            print('Vocẽ ja usou o maximo de ajudas, boa sorte.')
