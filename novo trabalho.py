import random

def pop_pobre(lista, elemento):
    nova_lista = []
    for item in lista:
        if item != elemento:
            nova_lista.append(item)
    return nova_lista

def meu_pop(lista, indice):
    elemento_removido = lista[indice]
    nova_lista = lista[:indice] + lista[indice+1:]
    return nova_lista

# def existe (vetor,numero):
#     for n in vetor:
#         if n == numero:
#             return True
#     return False

#def faz_o_quadrante()

def quadrante(dificuldade, quantidade_de_letra):
    if dificuldade == 4 or dificuldade == 6:
        alfabeto_original = list(range(65,91))
        alfabeto_aleatorio = []
        for _ in range(quantidade_de_letra):
            indice_aleatorio = random.randint(0,len(alfabeto_original)-1)
            letra_aleatoria = chr(alfabeto_original[indice_aleatorio])
            alfabeto_aleatorio.append(letra_aleatoria)
            alfabeto_original = pop_pobre(alfabeto_original,alfabeto_original[indice_aleatorio])
        alfabeto_aleatorio += alfabeto_aleatorio
        quadrante_original = [[ 0 for _ in range(dificuldade)] for _ in range(dificuldade)]
        
        for linha in range(len(quadrante_original)):
            for coluna in range(len(quadrante_original)):
                if len(alfabeto_aleatorio) > 0:
                    indice_aleatorio_quadrante = random.randint(0,(len(alfabeto_aleatorio)-1))
                    quadrante_original[linha][coluna] = alfabeto_aleatorio[indice_aleatorio_quadrante]
                    alfabeto_aleatorio = meu_pop(alfabeto_aleatorio,indice_aleatorio_quadrante)
                    
        for l in range(len(quadrante_original)):
            for c in range(len(quadrante_original)):
                print(quadrante_original[l][c],' ', end='')
            print('')
        return quadrante_original
    else:
        print('meu pai ta duro!')
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
        dificul_escolhida, numero_letra = 4 , 8
    elif escolhendo_a_dificulade == 2:
        dificul_escolhida, numero_letra = 6 , 18
    else:        
        dificul_escolhida, numero_letra = 8 , 32
 
    
    quadrante(6,18)
    #while True:
        #ler_entrada()
    