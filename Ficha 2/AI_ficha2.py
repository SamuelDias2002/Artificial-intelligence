import csv
import networkx as nx

# Abre o ficheiro e cria o grafo


def abrir():
    f = open("grafo.txt", "r")
    leitura = csv.reader(f)
    grafo = nx.Graph()

    for line in leitura:
        origem, destino, distancia = line
        distancia = int(distancia)
        grafo.add_edge(origem, destino, distancia=distancia)

    return grafo


# Encontra o caminho mais curto entre duas cidades
# Ex 2 - Hipotese 1
"""def encontrar_caminho(grafo, cidade_partida, cidade_destino):
    try:
        caminho = nx.shortest_path(
            grafo, cidade_partida, cidade_destino, weight='distancia')
        comprimento_total = sum(
            grafo[caminho[i]][caminho[i+1]]['distancia'] for i in range(len(caminho)-1))
    except nx.NetworkXNoPath:
        caminho = None
        comprimento_total = None

    return caminho, comprimento_total


grafo = abrir()
caminho_input = input(
    "Caminho (cidade de partida, cidade de destino): ").split(", ")
cidade_partida, cidade_destino = caminho_input

caminho, comprimento_total = encontrar_caminho(
    grafo, cidade_partida, cidade_destino)

if caminho:
    print(
        f"Caminho a percorrer entre a cidade de {cidade_partida} e a cidade de {cidade_destino}:")
    print(" -> ".join(caminho))
    print(f"Comprimento total do percurso: {comprimento_total}")
else:
    print(
        f"Não foi possível encontrar um caminho entre {cidade_partida} e {cidade_destino}.")"""

# Ex 2 - Hipotese 2


def encontrar_caminho(grafo, cidade_partida, cidade_destino):
    caminho = {}
    for u, v in nx.bfs_edges(grafo, cidade_partida):
        caminho[v] = u

        if v == cidade_destino:
            break

    if cidade_destino not in caminho:
        return None, None

    # Reconstruir o caminho
    caminho_completo = [cidade_destino]
    while cidade_destino != cidade_partida:
        cidade_destino = caminho[cidade_destino]
        caminho_completo.insert(0, cidade_destino)

    comprimento_total = sum(grafo[caminho_completo[i]][caminho_completo[i+1]]
                            ['distancia'] for i in range(len(caminho_completo) - 1))

    return caminho_completo, comprimento_total


# Carregar o grafo
grafo = abrir()

# Solicitar entrada do usuário
caminho_input = input(
    "Caminho (cidade de partida, cidade de destino): ").split(", ")
cidade_partida, cidade_destino = caminho_input

# Encontrar o caminho
caminho, comprimento_total = encontrar_caminho(
    grafo, cidade_partida, cidade_destino)

if caminho:
    print(
        f"Caminho a percorrer entre a cidade de {cidade_partida} e a cidade de {cidade_destino}:")
    print(" -> ".join(caminho))
    print(f"Comprimento total do percurso: {comprimento_total}")
else:
    print(
        f"Não foi possível encontrar um caminho entre {cidade_partida} e {cidade_destino}.")
