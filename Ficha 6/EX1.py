import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

tree.plot_tree(clf)

teste1 = [2.1, 2.7, 3.9, 1.2]
print(clf.predict([teste1], True))


plt.show()