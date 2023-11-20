import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('CTG.csv')
X = data[:, 0:21]
Y = data[:, 21]

# Conjuntos de teste e de treino
testX = X[:126]
testY = Y[:126]

treinoX = X[126:]
treinoY = Y[126:]

size = [100, 200, 500, 1000, 2000]
arr = []

for i in size:
    tX = treinoX[:i]
    tY = treinoY[:i]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(tX, tY)
    yPredict = clf.predict(testX)


curve_values = 0

for a, b in zip(testY, yPredict):
    if a == b:
        curve_values += 1
    print(i)
    print(curve_values)
    print(curve_values/126)
    arr.append(curve_values/126)

plt.plot(size, arr)
plt.show()
