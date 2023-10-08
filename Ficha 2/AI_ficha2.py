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

# Ex 2
def encontrar_caminho_Ex2(grafo, cidade_partida, cidade_destino):
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

# Ex 3
def encontrar_caminho_astar_Ex3(grafo, cidade_partida, cidade_destino):
    try:
        caminho_completo = nx.astar_path(grafo, cidade_partida, cidade_destino,heuristic=None, weight='distancia') 
# Como a função nx.astar_path cria internamente uma heurística que minimiza a distância entre 2 nodos, logo não precisamos de definir a função heurística
        comprimento_total = sum(grafo[caminho_completo[i]][caminho_completo[i+1]] ['distancia'] for i in range(len(caminho_completo) - 1))
        return caminho_completo, comprimento_total
    except nx.NetworkXNoPath:
        return None, None

# "Main"
# Carregar o grafo
grafo = abrir()

# Solicitar entrada do usuário
caminho_input = input(
    "Caminho (cidade de partida, cidade de destino): ").split(", ")
cidade_partida, cidade_destino = caminho_input

# Encontrar o caminho Ex2
caminho, comprimento_total = encontrar_caminho_Ex2(grafo, cidade_partida, cidade_destino)

# Encontrar o caminho Ex3
caminho,comprimento_total = encontrar_caminho_astar_Ex3(grafo, cidade_partida, cidade_destino)


if caminho:
    print(
        f"Caminho a percorrer entre a cidade de {cidade_partida} e a cidade de {cidade_destino}:")
    print(" -> ".join(caminho))
    print(f"Comprimento total do percurso: {comprimento_total}")
else:
    print(
        f"Não foi possível encontrar um caminho entre {cidade_partida} e {cidade_destino}.")

print("\n\n\n")

# Ex 4
def realizar_experiencia(grafo, cidade_partida, cidade_destino):
    caminho_ppl, comprimento_ppl = encontrar_caminho_Ex2(grafo, cidade_partida, cidade_destino)
    caminho_astar, comprimento_astar = encontrar_caminho_astar_Ex3(grafo, cidade_partida, cidade_destino)
    
    return comprimento_ppl, comprimento_astar



# Inicializar variáveis para armazenar os resultados
resultados_ppl = []
resultados_astar = []

# Realizar as experiências
for i in range(0, 2): # Alterar o range consoante o nr de experiencias a realizar
    caminho_input = input(
        f"Experiência {i}: Caminho (cidade de partida, cidade de destino): ").split(", ")
    cidade_partida, cidade_destino = caminho_input
    
    dist_ppl, dist_astar = realizar_experiencia(grafo, cidade_partida, cidade_destino)
    resultados_ppl.append(dist_ppl)
    resultados_astar.append(dist_astar)

# Calcular a média das distâncias obtidas para cada tipo de pesquisa
media_ppl = sum(resultados_ppl) / len(resultados_ppl)
media_astar = sum(resultados_astar) / len(resultados_astar)

# Imprimir a tabela
print("\nTabela de Resultados:")
print("Experiência | PPL (Km)  | A* (Km)")

for i in range(2): # Alterar o range consoante o nr de experiencias a realizar
    print(f"{i+1}           | {resultados_ppl[i]:.2f}    | {resultados_astar[i]:.2f}")

print(f"Média       | {media_ppl:.2f}    | {media_astar:.2f}")