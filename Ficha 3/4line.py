# coding: utf8
import copy
import random
import time

# ------------------------------------------------------------------


def mostra_tabuleiro(T):
    for i in range(0, 3):
        for j in range(0, 4):
            # O cálculo i * 3 + j converte as coordenadas (linha, coluna) em um índice na lista T,
            action = T[i*4 + j]
            # permitindo acessar o valor naquela posição do tabuleiro.
            if action == 0:
                print("-", end=" ")
            elif action == 1:
                print("X", end=" ")
            elif action == -1:
                print("O", end=" ")
        print()
# Devolve a lista de ações que se podem executar partido de um estado


def acoes(T):
    available_positions = []
    for i in range(3 * 4):
        if T[i] == 0:
            available_positions.append(i)
    return available_positions

# A função "resultado" deve ser ajustada para lidar com as posições
def resultado(T, pos, jog):
    aux = copy.copy(T)
    if aux[pos] == 0:
        aux[pos] = 1 if jog == 'MAX' else -1
    return aux
# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador


def utilidade(T):
    # Testa as linhas
    for i in (0, 1, 4, 5, 8, 9):
        if T[i] != 0 and T[i] == T[i + 1] and T[i] == T[i + 2]:
            return T[i]
    # Testa as colunas
    for i in (0, 1, 2, 3):
        if T[i] != 0 and T[i] == T[i + 4] and T[i] == T[i + 8]:
            return T[i]
    # Testa as diagonais
    if T[0] == T[5] == T[10] and T[2] == T[5] == T[8] and T[i] != 0:
        return T[5]
    if T[1] == T[6] == T[11] and T[3] == T[6] == T[9] and T[i] != 0:
        return T[6]
    # Não é nodo folha ou dá empate
    if 0 not in T:
        return 0
    return None

# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False


def estado_terminal(T):
    return utilidade(T) is not None or all(pos != 0 for pos in T)


# ------------------------------------------------------------------
# algoritmo da wikipedia
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
def alfabeta(T, alfa, beta, jog):
    if estado_terminal(T):
        return utilidade(T), -1, -1
    if jog:
        v = -10
        ba = -1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MAX'), alfa, beta, False)
            if v1 > v:
                v = v1
                ba = a
            alfa = max(alfa, v)
            if v >= beta:
                break
        return v, ba, resultado(T, ba, 'MAX')
    else:
        v = 10
        ba = -1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MIN'), alfa, beta, True)
            if v1 < v:
                v = v1
                ba = a
            beta = min(beta, v)
            if v <= alfa:
                break
        return v, ba, resultado(T, ba, 'MIN')
# ------------------------------------------------------------------


def joga_max(T):
    v, a, e = alfabeta(T, -10, 10, True)
    print("MAX joga para", a)
    return e

# ------------------------------------------------------------------

def joga_min(T):
    v, a, e = alfabeta(T, -10, 10, False)
    print("MIN joga para", a)
    return e

# ------------------------------------------------------------------


def jogo(p1, p2):
    # cria tabuleiro vazio
    T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    mostra_tabuleiro(T)
    while acoes(T) != [] and not estado_terminal(T):
        T = p1(T)
        mostra_tabuleiro(T)
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)
            mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        print("\nVenceu o MAX\n")
    elif utilidade(T) == -1:
        print("\nVenceu o MIN\n")
    else:
        print("\nEmpate\n")

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand(T):
    while True:
        x = random.randint(0, 11)  # Intervalo válido de índices
        if T[x] == 0:
            T[x] = -1
            break
    return T

# ------------------------------------------------------------------
def jogo_1000x():
    num_vitorias_max = 0
    num_vitorias_random = 0
    num_empates = 0
    total_tempo = 0

    for _ in range(20):
        T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        inicio = time.time()
        jogo(joga_max, joga_rand)
        resultado_jogo = utilidade(T)
        if resultado_jogo == 1:
            num_vitorias_max = num_vitorias_max + 1
        elif resultado_jogo == -1:
            num_vitorias_random =  num_vitorias_random + 1
        else:
            num_empates = num_empates + 1
        fim = time.time()
        total_tempo += (fim - inicio)

    print("\nTempo para executar os 20 jogos (segundos):\n", total_tempo)

    ###print("\nVitórias do MAX:\n", num_vitorias_max)
    ###print("\nVitórias do RAND:\n", num_vitorias_random)
    ###print("\nEmpates:\n", num_empates)"""


# main
# deve ganhar sempre o max:
# jogo(joga_max, joga_rand)
# devem empatar sempre:
#jogo(joga_max, joga_min)


"""Problema: 
O max ganha sempre ao min, como suposto devido ao facto de ser o primeiro a jogar, pois quem joga primeiro tem vantagem.
Quando é max vs random, o max ganha sempre, o que nem sempre é suposto """
jogo_1000x()    
