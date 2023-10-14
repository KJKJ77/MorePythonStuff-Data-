from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(iris.data,iris.target)

newData = [[6.4, 3.1, 4.4, 1.2]]
print(classifier.predict(newData))
