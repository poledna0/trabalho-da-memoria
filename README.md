# Jogo da memória
O jogo da memória consiste em apresentar pares de desenhos<br>
distribuídos em quadrantes e o jogador deve adivinhar as posições que<br>
apresentam desenhos iguais. No exemplo abaixo, o quadrante [0,0] e o<br>
[3,2] apresentam o mesmo desenho, o sol.
# 2. Requisitos Mínimos:
Um cliente solicitou a turma uma implementação deste jogo em<br>
linguagem Python, a ser executado via terminal (modo texto).<br> O cliente
também apresentou uma série de requisitos detalhados a seguir.<br>
2. Requisitos Mínimos:
<br>a. 3 Níveis de dificuldade: Matrizes 4x4, 6x6 e 8x8
Utilizar letras maiúsculas apenas (A-Z).
<br>b. Na matriz de exibição, as respostas devem estar ocultas por
um “#”. A células que já foram acertadas devem ser exibidas.
<br>c. Uma opção “exibir respostas” pode ser ativada por 3
segundos, no máximo 2 vezes por jogo. Neste caso, a matriz
deve ser exibida sem os ‘#’
<br>d. Gráficos em Turtle (opcional, 2 pts extras) 
<br>e. O jogo encerra ao descobrir todas as respostas ou
desistência.
# Funções Mínimas Exigidas:
def criar_matriz(dificuldade):<br>
aqui é criada as matrizes de acordo com a dificuldade<br>
return mat, mat_exib<br>
def atualiza(pos1, pos2, mat, mat_exib):<br>
verifica se os pares de símbolos conferem<br>
e atualiza matriz<br>
obs: pode-se considerar pos1,pos2 uma tupla [linha,coluna]
exemplo:<br>
pos1=[0,0] ou seja, x=0,y =0<br>
pos2=[3,5] ou seja, x=3,y =5<br>
return mat, mat_exib<br>
def exibir_resp(mat):<br>
exibe a matriz resposta por 5 segundos<br>
 no maximo 2x<br>
return<br>
*Obs: As váriaveis das funções não podem estar declaradas
globalmente. Elas devem estar no contexto da função;

# TIPOS DE DADOS E ESTRUTURAS PERMITIDAS
 Int<br>
 Float<br>
 Char<br>
 Vetores e Matrizes<br>
 IF, ELSE, ELSIF<br>
 FOR, WHILE<br>
 Funções<br>
# 3. NÃO É PERMITIDO:
Bibliotecas externas não são permitidas. Ou seja, também não se
pode utilizar funções pré-definidas (built-in) pelo python que
minimizem a lógica de implementação, tal como max(), min(),
isdigit(), ischar(), sorted(), ‘if ... in ...’ etc. Como já vimos, todas as
funções são perfeitamente implementáveis. Qualquer função necessária deve ser implementada pelo programador. Também não
utilizar váriaveis globais.
Time(), randonint(), clear() e/ou similares estão liberadas
# 4. Avaliação e Considerações
- Grupos de até 5 pessoas.<br>
- Entrega 12/06 até 19:00 via AVA INSTITUCIONAL (Aba
Tarefas)<br>
- Enviar Código-Fonte<br>
- Inserir os integrantes do grupo em comentário no código, nas
primeiras linhas<br>
- Apenas 1 envio por grupo (cadastrar grupos no ava)<br>
- Arquivos que não executem, apresente erros de sintaxe, será
atribuído nota ZERO.<br>
- Não haverá postergação do prazo de entrega<br>
- Prova de autoria (individual), se o professor achar necessário,
cabendo alteração de nota de acordo com o desempenho do aluno.<br>
- Será atribuído ZERO nos casos de cola. (Score de plágio pela
ferramenta MOSS)<br>
- A solução será avaliada quanto a adequação da lógica de<br>
programação, utilização de estruturas de controle e repetição, a correta
utilização de variáveis, tipos de dados e modularização de código
(funções).<br>
- Boas práticas de programação, como formatação de código,
nomenclatura de variáveis também fazem parte da avaliação.
Raciocínio Algorítmico - Prof. André Gustavo Hochuli<br>
