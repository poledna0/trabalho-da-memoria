# Henrique Poledna, Eduardo Machado, Leonardo de Goes da Silva, Luis Henrique Hiroyuki

import random
import time

def loop_imprimir(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro)):
            print(tabuleiro[linha][coluna],' ', end='')
        print('')
        
def pop_pobre(lista, elemento, indice, qual_pop):
    if qual_pop == 1:
        nova_lista = []
        for item in lista:
            if item != elemento:
                nova_lista.append(item)
        return nova_lista
    else:
        nova_lista = lista[:indice] + lista[indice+1:]
        return nova_lista
    
def faz_o_quadrante(dificuldade, alfabeto_copia):
    quadrante_original = [[ 0 for _ in range(dificuldade)] for _ in range(dificuldade)]
    for linha in range(len(quadrante_original)):
        for coluna in range(len(quadrante_original)):
            if len(alfabeto_copia) > 0:
                indice_aleatorio_quadrante = random.randint(0,(len(alfabeto_copia)-1))
                quadrante_original[linha][coluna] = alfabeto_copia[indice_aleatorio_quadrante]
                alfabeto_copia = pop_pobre(alfabeto_copia,0,indice_aleatorio_quadrante,2)
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
        alfabeto_original = pop_pobre(alfabeto_original,alfabeto_original[indice_aleatorio],0,1)
    alfabeto_aleatorio += alfabeto_aleatorio
    return alfabeto_aleatorio

def cria_matriz (dificuldade, quantidade_de_letra):
    if dificuldade == 4 or dificuldade == 6:
        vet = alfabeto_aleatorios(dificuldade, quantidade_de_letra)
        somavet = faz_o_quadrante(dificuldade, vet)
    else:
        quantidade_de_letra = 26
        vet = alfabeto_aleatorios(dificuldade, quantidade_de_letra)
        vet += ['0','0','1','1','2','2','3','3','4','4','5','5']
        somavet = faz_o_quadrante(dificuldade, vet)
    return somavet
        
def atualiza(tabu):
    vetor_ind = []
    vetor_let = []
    for _ in range(2):
        linha_entrada = int(input('Digite uma linha: '))
        coluna_entrada = int(input('Digite uma coluna: '))
        print('')
        vetor_ind.append(linha_entrada)
        vetor_ind.append(coluna_entrada)
    if vetor_ind[0] == vetor_ind[2] and vetor_ind[1] == vetor_ind[3]:
        print('Não pode ser a mesma posição')
    else:
        if tabu[vetor_ind[0]][vetor_ind[1]] == tabu[vetor_ind[2]][vetor_ind[3]]:
            vetor_let.append(tabu[vetor_ind[0]][vetor_ind[1]])
    return vetor_let

def esconde_matriz(tabuleiro, vetor_com_letrinhas): 
    tabuleiro_escondido = [['#' for _ in range(len(tabuleiro))] for _ in range(len(tabuleiro))]
    for l in range(len(tabuleiro)):
        for c in range(len(tabuleiro)):
            if tabuleiro[l][c] in vetor_com_letrinhas:
                tabuleiro_escondido[l][c] = tabuleiro[l][c]
    loop_imprimir(tabuleiro_escondido)        

def exibir_resp(variavel,tabuleiro):
    entrada = int(input('Você quer ajuda?\nPodemos mostrar o tabuleiro por 5 segundos.\n[1] Sim\n[2] Não\n>>>'))
    if entrada == 1:
        loop_imprimir(tabuleiro)
        time.sleep(3)
        variavel += 1
    return variavel   

def desisti():
    desistir = int(input('Deseja desistir?\n[1] Sim\n[2] Não\n>>>'))
    if desistir == 1:
        print('Fim de Jogo')
        return True
    else:
        return False
   
if __name__ == "__main__":
    escolhendo_a_dificulade =int(input('Digite a dificulade:\n[1] Fácil\n[2] Médio\n[3] Hardcore\n>>>'))
    vetor_com_letras = []
    contador_de_ajuda = 0
    if escolhendo_a_dificulade == 1:
        dificul_escolhida, numero_letra = 4 , 8
    elif escolhendo_a_dificulade == 2:
        dificul_escolhida, numero_letra = 6 , 18
    else:        
        dificul_escolhida, numero_letra = 8 , 32
    quadrante = cria_matriz(dificul_escolhida,numero_letra)
    time.sleep(5)
    print('\033c', end='')
    while True:
        vetor_com_letras += atualiza(quadrante)
        esconde_matriz(quadrante,vetor_com_letras)
        if contador_de_ajuda < 3: 
            contador_de_ajuda += exibir_resp(contador_de_ajuda,quadrante)
            print('\033c', end='')
            esconde_matriz(quadrante,vetor_com_letras)
        if len(vetor_com_letras) == numero_letra:
            print('Parabéns, você venceu!')
            break
        if desisti():
            break
