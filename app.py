import tensorflow as tf
import keras
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle
import sklearn

data = pd.read_csv("student-mat.csv", sep=";")

# print first 5 rows
# print(data.head())
data = data[["G1", "G2", "G3", "studytime", "failures", "absences", "Dalc", "Walc", "health", "studytime", "traveltime", "goout", "freetime", "Medu"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

acc = linear.score(x_test, y_test)
print(acc)

print("cef: ", linear.coef_)
print("interc: ", linear.intercept_)

predicts = linear.predict(x_test)