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

def faz_o_quadrante(dificuldade, alfabeto_copia):
    quadrante_original = [[ 0 for _ in range(dificuldade)] for _ in range(dificuldade)]
    for linha in range(len(quadrante_original)):
        for coluna in range(len(quadrante_original)):
            if len(alfabeto_copia) > 0:
                indice_aleatorio_quadrante = random.randint(0,(len(alfabeto_copia)-1))
                quadrante_original[linha][coluna] = alfabeto_copia[indice_aleatorio_quadrante]
                alfabeto_copia = meu_pop(alfabeto_copia,indice_aleatorio_quadrante)
            print(quadrante_original[linha][coluna],' ', end='')
        print('')
    return quadrante_original

def alfabeto_aleatorios (dificuldade, quantidade_de_letra):
    alfabeto_original = list(range(65,91))
    alfabeto_aleatorio = []
    for _ in range(quantidade_de_letra):
        indice_aleatorio = random.randint(0,len(alfabeto_original)-1)
        letra_aleatoria = chr(alfabeto_original[indice_aleatorio])
        alfabeto_aleatorio.append(letra_aleatoria)
        alfabeto_original = pop_pobre(alfabeto_original,alfabeto_original[indice_aleatorio])
    alfabeto_aleatorio += alfabeto_aleatorio
    faz_o_quadrante(dificuldade, alfabeto_aleatorio)
    return alfabeto_aleatorio

def alfabeto (dificuldade, quantidade_de_letra):
    
    if dificuldade == 4 or dificuldade == 6:
        v = alfabeto_aleatorios(dificuldade, quantidade_de_letra)
    else:
        v = alfabeto_aleatorios(dificuldade, quantidade_de_letra)
        v += ['0','1','2','3','4','5']
    return v
        
def ler_entrada():
    vetor = []
    for _ in range(2):
        linha_entrada = int(input('Digite uma linha: '))
        coluna_entrada = int(input('Digite uma coluna: '))
        vetor.append(linha_entrada)
        vetor.append(coluna_entrada)
    return vetor


if __name__ == "__main__":

    escolhendo_a_dificulade = 0#int(input('Digite a dificulade: facil-1 , medio-2 , dificil-3: '))

    if escolhendo_a_dificulade == 1:
        dificul_escolhida, numero_letra = 4 , 8
    elif escolhendo_a_dificulade == 2:
        dificul_escolhida, numero_letra = 6 , 18
    else:        
        dificul_escolhida, numero_letra = 8 , 32
 
    
    alfabeto(6,18)
    #while True:
        #ler_entrada()
    