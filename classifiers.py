import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn import metrics
import sklearn


# Set training and testing data
def splitData(data):
    predict = "salary_minimum"
    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    return x_train, x_test, y_train, y_test


# Create a linear regression Classifier
def linearRegressionClassifier(data):
    x_train, x_test, y_train, y_test = splitData(data)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)
    accLin = linear.score(x_test, y_test)
    print("Linear acc: ", accLin * 100)


# Create a Gaussian Classifier
def gaussianNBClassifier(data):
    x_train, x_test, y_train, y_test = splitData(data)
    naive = GaussianNB()
    naive.fit(x_train, y_train)
    y_pred = naive.predict(x_test)
    accNaive = metrics.accuracy_score(y_test, y_pred)
    print("Naive Acc: ", accNaive * 100)


# Create a KNN Classifier
def knnClassifier(data):
    x_train, x_test, y_train, y_test = splitData(data)
    knn = KNeighborsClassifier(n_neighbors=10)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    accKNN = metrics.accuracy_score(y_test, y_pred)
    print("KNN Acc: ", accKNN)


# sys.modules[__name__] = linearRegressionClassifier, gaussianNBClassifier, knnClassifier
