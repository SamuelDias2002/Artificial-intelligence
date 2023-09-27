
import networkx as nx
import csv

G = nx.Graph()

f = open("grafo.txt", "r")
leitura = csv.reader(f)
for line in leitura:
        origem, destino, distancia = line
        distancia = int(distancia)
        G.add_edge(origem,destino,distancia = distancia)

print ("Cidade -> Cidade(s) Vizinha(s) \n")
for cidade in G.nodes:
    vizinho = list(G.neighbors(cidade))
    print(f" {cidade} -> {', '.join(vizinho)}")

print("\n") 