# FICHA 1 / 1st Pratical Class


# EX 1

x = range(10, 34)
for n in x:
  if n%2 != 0:
    print(n, end = " ")


# EX 2

x = int (input ())
if x > 100 or x < 0:
  print ("Error")
else:
  dezenas = x // 10
  unidades = x // 1
  print (dezenas)
  print (unidades)


# EX 3

def ler ():
  x = input()
  print (x)

def gravar():
  x = input()
  text = open ("file", "w")
  text.write (x)
  text.close


def contavogal(v):
  x = input()
  i = int( x.count("a")+x.count("e")+x.count("i")+x.count("o")+x.count("u"))
  print (i)


# EX 4
def ler_lista():
    lista = []
    while True:
        numero = int(input())
        if numero < 0:
            break
        lista.append(numero) #Append
    return lista

def encontrar_intersecao(lista1, lista2):
    intersecao = []
    for elemento in lista1:
        if elemento in lista2:
            intersecao.append(elemento)
    return intersecao

print("Digite a primeira lista:")
lista1 = ler_lista()
print("Digite a segunda lista:")
lista2 = ler_lista()
resultado = encontrar_intersecao(lista1, lista2)
if resultado:
    print("Elementos que aparecem em ambas as listas:")
    print(resultado)
else:
    print("Não há elementos em comum nas duas listas.")


# EX 5 


import numpy as np


print("Digite os elementos da matriz A 2x2:")
a = np.array([[float(input()), float(input())], [float(input()), float(input())]])

print("Digite os elementos da matriz B 2x2:")
b = np.array([[float(input()), float(input())], [float(input()), float(input())]])

# (a) 
produto_elemento_a_elemento = a * b

# (b) 
produto_matricial = np.dot(a, b)

# (c) 
diferenca_matrizes = a - b

# (d)
log_a = np.log(np.abs(a))

# (e) 
maior_valor_segunda_linha_a = np.max(a[1, :])
menor_valor_primeira_coluna_b = np.min(b[:, 0])
resultado_e = maior_valor_segunda_linha_a * menor_valor_primeira_coluna_b

print("\n(a) Produto elemento a elemento A.B:")
print(produto_elemento_a_elemento)

print("\n(b) Produto matricial A * B:")
print(produto_matricial)

print("\n(c) Diferença entre matrizes A - B:")
print(diferenca_matrizes)

print("\n(d) Logaritmo dos elementos de A:")
print(log_a)

print("\n(e) Maior valor da segunda linha de A vezes o menor valor da primeira coluna de B:")
print(resultado_e)


# Ex 6
notas = {}

def inserir_nota(): 
    uc = input("Digite o nome da UC: ")
    nota = float(input("Digite a nota obtida na UC: "))
    notas[uc] = nota
    print ("Inserido com sucesso")

def alterar_nota():
    uc = input("Digite o nome da UC que deseja alterar a nota: ")
    if uc in notas:
        nova_nota = float(input("Digite a nova nota: "))
        notas[uc] = nova_nota
        print(f"Nota para {uc} alterada com sucesso!") # f serve para substituir {uc} pelo input dado 
    else:
        print(f"A UC {uc} não foi encontrada!")

def calculo_media():
  if notas:
        media = sum(notas.values()) / len(notas)
        print(f"A média das notas é: {media:.2f}") #.2f para limitar os valores a 2 casas decimais
  else:
        print("Nenhuma nota inserida.")

def mostrar_notas():
  print ("NOTAS DA UC")
  for uc, nota in notas.items():
     print(f"{uc}: {nota}")

while True:
    print("1. Inserir nota")
    print("2. Alterar nota")
    print("3. Mostrar todas as notas")
    print("4. Calcular a média")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        inserir_nota()
    elif opcao == '2':
            alterar_nota()
    elif opcao == '3':
            mostrar_notas()
    elif opcao == '4':
            calculo_media()
    elif opcao == '5':
            break
    else:
          print("Escolha uma opção válida!")

# EX 7


frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")
conjunto1 = set(frase1)
conjunto2 = set(frase2)

letras_em_ambas_frases = conjunto1.intersection(conjunto2)
letras_apenas_na_primeira = conjunto1.difference(conjunto2)
letras_em_ambas = conjunto1.intersection(conjunto2)
letras_apenas_na_primeira_ou_segunda = conjunto1.symmetric_difference(conjunto2)

print("\n(a) Todas as letras que aparecem em ambas as frases:")
print(letras_em_ambas_frases)

print("\n(b) As letras que aparecem na primeira frase mas não na segunda:")
print(letras_apenas_na_primeira) 



print("\n(c) As letras que aparecem simultaneamente em ambas as frases:")
print(letras_em_ambas)

print("\n(d) As letras que só aparecem na primeira frase ou só aparecem na segunda frase:")
print(letras_apenas_na_primeira_ou_segunda)


# EX 8 

import networkx as nx
import csv

G = nx.Graph()

f = open("grafo.txt", "r")
leitura = csv.reader(f)
for line in leitura:
        origem, destino, distancia = line
        distancia = int(distancia)
        G.add_edge(origem,destino,distancia = distancia)
print ("        Cidade -> Cidade(s) Vizinha(s)")
for cidade in G.nodes:
    vizinho = list(G.neighbors(cidade))
    print(f" {cidade} -> {', '.join(vizinho)}")