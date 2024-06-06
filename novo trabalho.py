import random

# def quadrante(dificul): # pensei em ainda deixar em ascii e fazer um ocntador que vai colocar a mesma letra se o contador estiver em 1, quando chegar em dois ele gera outro numero ascii
#     alfabeto_aleatorio = []

#     while len(alfabeto_aleatorio) < dificul:
#         numero_aleatorio = random.randint(65,90)
#         if existe(alfabeto_aleatorio, numero_aleatorio):
#             None
#         else:
#             alfabeto_aleatorio.append(numero_aleatorio)
#     for indice, numero in enumerate (alfabeto_aleatorio):
#         alfabeto_aleatorio[indice] = chr(numero)

#     print(alfabeto_aleatorio)
# def existe (vetor,numero):
#     for n in vetor:
#         if n == numero:
#             return True
#     return False
# def quadrante(dific):
#     quadrante1 = [[random.randint(0, 24) for _ in range(dific)] for _ in range(dific)]
#     print(quadrante1)
#     quadrante2 = [[elemento for elemento in linha] for linha in quadrante1]
#     print(quadrante2)
#     quadrante_final = [[], []]
#     quadrante_final[0] = quadrante1
#     quadrante_final[1] = quadrante2
#     print(quadrante_final)

#----------------------------------------------------------------------------------------------------------------------------
# Percorrer um range de 65 até 90 e depois um rande de 1 - x(definida na variavel de dificulade) dando um total de 32 "figuras", cada figura precisa de duas localizações com random e o random nao pode se repetir mais do que uma vez
#----------------------------------------------------------------------------------------------------------------------------


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
    #     dificul_escolhida = 2
    # elif escolhendo_a_dificulade == 2:
    #     dificul_escolhida = 3
    # else:
    #     dificul_escolhida = 4

    # quadrante(dificul_escolhida)
    quadrante(4)

    #while True:
        #ler_entrada()
        
