import random

def pop_pobre (vetor, numero):
    nova_lista = []
    for numero_da_lista in vetor:
        if numero_da_lista != numero:
            nova_lista.append(numero_da_lista)
    return nova_lista

def existe (vetor,numero):
    for n in vetor:
        if n == numero:
            return True
    return False

def quadrante(dificuldade, quantidade_de_letra):
    # obra de arte do semestre : 
    alfabeto_original = list(range(65,91))
    alfabeto_aleatorio = []
    vetor_clone = []
    for _ in range(quantidade_de_letra):
        #escolhe o indice para pegar um numero do alfabeto original
        indice_aleatorio = random.randint(0,len(alfabeto_original)-1)
        # transforma em letra
        letra_aleatoria = chr(alfabeto_original[indice_aleatorio])
        # add a letra em um vetor
        alfabeto_aleatorio.append(letra_aleatoria)
        # ele apaga o numero q pegou da lista principal para n pegar dnv
        lista_nova = pop_pobre(alfabeto_original,alfabeto_original[indice_aleatorio])
        # atualiza o alfabeto orig
        alfabeto_original = lista_nova
    print(alfabeto_aleatorio)
    print(alfabeto_original)
    vetor_clone += alfabeto_aleatorio
    print(vetor_clone)
    quadrante_origina = list(range(dificuldade)for _ in range(dificuldade))
    print(quadrante_origina)

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

    escolhendo_a_dificulade = 0#int(input('Digite a dificulade: facil-1 , medio-2 , dificil-3: '))

    if escolhendo_a_dificulade == 1:
         dificul_escolhida = 2
    elif escolhendo_a_dificulade == 2:
         dificul_escolhida = 3
    else:
         dificul_escolhida = 4
    
    quadrante(4,8)

    #while True:
        #ler_entrada()