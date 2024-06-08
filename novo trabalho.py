import random

def pop_pobre (vetor, numero):
    nova_lista = []
    for numero_da_lista in vetor:
        if numero_da_lista != numero:
            nova_lista.append(numero_da_lista)
    return nova_lista

def quadrante(dificuldade):

    alfabeto_original = list(range(65,91))
    alfabeto_aleatorio = []
    for _ in range(26):
        indice_aleatorio = random.randint(0,len(alfabeto_original)-1)
        letra_aleatoria = chr(alfabeto_original[indice_aleatorio])
        alfabeto_aleatorio.append(letra_aleatoria)
        lista_nova = pop_pobre(alfabeto_original,alfabeto_original[indice_aleatorio])
        alfabeto_original = lista_nova  # Atualiza alfabeto_original
    print(alfabeto_aleatorio)
    print(alfabeto_original)

def existe (vetor,numero):
    for n in vetor:
        if n == numero:
            return True
    return False

def ler_entrada():
    vetor = []
    for _ in range(2):
        linha_entrada = int(input('Digite uma linha: '))
        coluna_entrada = int(input('Digite uma coluna: '))
        vetor.append(linha_entrada)
        vetor.append(coluna_entrada)
    return vetor

#----------------------------------------------------------------------------------------------------------------------------
# Percorrer um range de 65 até 90 e depois um rande de 1 - x(definida na variavel de dificulade) dando um total de 32 "figuras", cada figura precisa de duas localizações com random e o random nao pode se repetir mais do que uma vez
#----------------------------------------------------------------------------------------------------------------------------




if __name__ == "__main__":

    # escolhendo_a_dificulade = int(input('Digite a dificulade: facil-1 , medio-2 , dificil-3: '))

    # if escolhendo_a_dificulade == 1:
    #     dificul_escolhida = 2
    # elif escolhendo_a_dificulade == 2:
    #     dificul_escolhida = 3
    # else:
    #     dificul_escolhida = 4

    # quadrante(dificul_escolhida)
    quadrante(4)

    #while True:
        #ler_entrada()