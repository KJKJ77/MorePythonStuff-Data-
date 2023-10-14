from sklearn import tree
from sklearn.datasets import load_iris
from io import StringIO  
import pydotplus

iris = load_iris()

classifier = tree.DecisionTreeClassifier()
classifier.fit(iris.data,iris.target)

#visualize 
dot_data = StringIO()
tree.export_graphviz(classifier, out_file=dot_data, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, special_characters=True )

graph =pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")


