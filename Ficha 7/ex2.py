from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

train = np.loadtxt('espiral_train.csv', delimiter=',')
teste = np.loadtxt('espiral_test.csv', delimiter=',')

treinoX = train[:, 0:2]
treinoY = train[:, -1]
testeX = teste[:, 0:2]
testeY = teste[:, -1]

clf = svm.SVC(C=1000)
clf.fit(treinoX, treinoY)

print(clf.predict(testeX))
print(clf.score(testeX, testeY))
