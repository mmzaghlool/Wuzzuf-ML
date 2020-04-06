import tensorflow as tf
import keras
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

data = pd.read_csv("Wuzzuf_Job_Posts_Sample.csv", sep=",")
columns = ["city", "job_title", "salary_minimum", "salary_maximum", "career_level", "experience_years",
           "job_category1", "job_category2", "job_category3", "job_industry1", "job_industry2", "job_industry3"]
data = data[columns]


def convertStringsToNumbers():
    # creating labelEncoder
    le = preprocessing.LabelEncoder()

    for i in columns:
        if (i == "salary_minimum") | (i == "salary_maximum") | (i == "num_vacancies"):
            continue

        data[i] = le.fit_transform(data[i])

    # print("data after transformation: ", data)

convertStringsToNumbers()

predict = "salary_minimum"
features = np.array(data.drop([predict], 1))
label = np.array(data[predict])

x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.1, random_state=109)

print("label:", label)
print("features:", features)

knn = KNeighborsClassifier(n_neighbors=5)

# Train the model using the training sets
knn.fit(x_train, y_train)

#Predict Output
y_pred = knn.predict(x_test)
print("Predicted Value:", y_pred)


acc = metrics.accuracy_score(y_test, y_pred)
print("Acc: ", acc)
