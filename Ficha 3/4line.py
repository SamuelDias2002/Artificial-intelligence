# coding: utf8
import copy
import random

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
    states = []
    for i in range(12, 0, -1):
        if T[i] == 0:
            states.append(i)
    return states


# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação


def resultado(T, a, jog):
    aux = copy.copy(T)
    if aux[a] == 0:
        if jog == 'MAX':
            aux[a] = 1
        elif jog == 'MIN':
            aux[a] = -1
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
    T = [0, 0, 0, 0,
         0, 0, 0, 0,
         0, 0, 0, 0]
    # podemos partir de um estado mais "avançado"
    # T = [1,-1,0,0,-1,0,1,0,0]
    mostra_tabuleiro(T)
    while acoes(T) != [] and not estado_terminal(T):
        T = p1(T)
        mostra_tabuleiro(T)
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)
            mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        print("Venceu o jog1")
    elif utilidade(T) == -1:
        print("Venceu o jog2")
    else:
        print("Empate")

# ------------------------------------------------------------------
# jogador aleatório


def joga_rand(T):
    x = random.randint(0, 12)
    if T[x] != 0:
        while T[x] != 0:
            x = random.randint(0, 12)
            T[x] = -1
    # COMPLETAR
    return T

# ------------------------------------------------------------------
# main


# deve ganhar sempre o max:
# jogo(joga_max, joga_rand)
# devem empatar sempre:
jogo(joga_max, joga_min)
