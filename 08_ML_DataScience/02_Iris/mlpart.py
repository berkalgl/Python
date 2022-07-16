from sklearn.datasets import load_iris

#https://en.wikipedia.org/wiki/Iris_flower_data_set
#https://scikit-learn.org/stable/
# this data is already clean
iris = load_iris()

# input
x = iris.data

# target
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

#3 spliting the data
# splits arrays or matrices into random train and test subsets
from sklearn.model_selection import train_test_split

# it returns what we call a dimensionality of the array
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.2)
print(X_train.shape) # 90 rows 4 columns
print(X_test.shape) # 60 rows 4 columns

#4 Creating a model
#we are using k-nearest neighbours
#https://scikit-learn.org/stable/modules/neighbors.html
#http://vision.stanford.edu/teaching/cs231n-demos/knn/
#https://www.analyticsvidhya.com/blog/2018/08/k-nearest-neighbor-introduction-regression-python/
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
# We can use any type of algorithm we want
# We can use Decision Tree Classifier as well
knn.fit(X_train, Y_train)
# testing
y_pred = knn.predict(X_test)
# we need to compare our prediction to test data sets
from sklearn import metrics
print(metrics.accuracy_score(Y_test, y_pred))
#0.966666666667 correctness

sample = [[3,5,4,2],[2,3,5,4]]
predictions = knn.predict(sample)
pred_species = [iris.target_names[p] for p in predictions]
print("predictions", pred_species)

# model persistence is important because next time 
# we want to make prediction. we want to save this model
# https://scikit-learn.org/stable/model_persistence.html
# saving the model
from joblib import dump, load
dump(knn, 'mlbrain.joblib')

# load
model = load('mlbrain.joblib')
model.predict(X_test)

# source 
#https://github.com/aneagoie/ML-Notes/blob/master/iris.ipynb