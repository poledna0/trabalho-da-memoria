import random

def quadrante(dificul): # pensei em ainda deixar em ascii e fazer um ocntador que vai colocar a mesma letra se o contador estiver em 1, quando chegar em dois ele gera outro numero ascii
    alfabeto_aleatorio = []
    while len(alfabeto_aleatorio) < 26:
        numero_aleatorio= random.randint(65,90)
        if existe(alfabeto_aleatorio, numero_aleatorio):
            None
        else:
            alfabeto_aleatorio.append(numero_aleatorio)
    for indice, numero in enumerate (alfabeto_aleatorio):
        alfabeto_aleatorio[indice] = chr(numero)

    print(alfabeto_aleatorio)
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

if __name__ == "__main__":

    # escolhendo_a_dificulade = int(input('Digite a dificulade: facil-1 , medio-2 , dificil-3: '))

    # if escolhendo_a_dificulade == 1:
    #     dificul_escolhida = 4
    # elif escolhendo_a_dificulade == 2:
    #     dificul_escolhida = 6
    # else:
    #     dificul_escolhida = 8

    # quadrante(dificul_escolhida)
    quadrante(4)

    #while True:
        #ler_entrada()
        