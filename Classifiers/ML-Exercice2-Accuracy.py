from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

#split: training and testing sets
X_train, X_test, y_train, y_test= train_test_split(X, y , test_size=0.5)

#train classifier
clf = tree.DecisionTreeClassifier()
clf.fit(X_train,y_train)

#predict for test data
predicitions = clf.predict(X_test)

print(accuracy_score(y_test,predicitions))