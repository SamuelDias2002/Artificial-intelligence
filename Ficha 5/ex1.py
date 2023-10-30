'''
IA
UBI
ex1

usando pyagrum
http://www-desir.lip6.fr/~phw/aGrUM/docs/last/notebooks/Tutorial.ipynb.html
https://pyagrum.readthedocs.io/en/0.22.2/

sudo pip3 install pyagrum

ou

pip3 install pyagrum

portas: A, B e C (e D no ex #3)
'''
import pyAgrum as gum

def mostra(d, q):
    # mostra resultado do query q, dadas as observações d
    global ie
    ie.setEvidence(d)
    ie.makeInference()
    print (ie.posterior(q))

def prob_monty(guess, prize):
    # define probabilidade de o monty escolher abrir cada porta, sabendo quais foram as outras 2 escolhas: devolve uma lista com a prob de abrir cada porta
    p = []
    for monty in ['A','B','C','D']:
        if guess == monty or prize == monty:
            p.append(0)
        elif guess == prize:
            p.append(1./3)  # Monty tem igual probabilidade de escolher entre as portas restantes
        else:
            p.append(0.5)  # Monty tem igual probabilidade de escolher entre as portas restantes
    return p



bn=gum.BayesNet('MontyHall')

# criar nodos
guess=bn.add(gum.LabelizedVariable('guest','guest',['A','B','C','D']))
prize=bn.add(gum.LabelizedVariable('prize','prize',['A','B','C','D']))
monty=bn.add(gum.LabelizedVariable('monty','monty',['A','B','C','D']))

# criar arestas
bn.addArc(guess,monty)
bn.addArc(prize,monty)

# colocar tabelas de probabilidade no nodos
# o convidado escolhe uma porta aleatóriamente
bn.cpt(guess)[{}] = [1./4,1./4,1./4,1./4] # 1/3 caso for 3 portas
# a porta que tem o prémio também pode ser qualquer
bn.cpt(prize)[{}] = [1./4,1./4,1./4,1./4] # 1/3 caso for 3 portas
# a porta escolhida pelo Monty depende das portas do guest e do prize
for i in ['A','B','C','D']:
    for j in ['A','B','C','D']:
        bn.cpt(monty)[{'guest': i, 'prize': j}] = prob_monty(i,j)
ie=gum.LazyPropagation(bn)

# passar os valores observados para algumas variáveis e ele estima a probabilidade das restantes

# exemplo: se o guest escolher a porta B e o prémio estiver na porta A, qual a prob de o monty escolher as várias portas?
mostra({ 'guest' : 'B' , 'prize' : 'A'}, 'monty')

mostra({'guest': 'B', 'monty': 'A'}, 'prize')

