import tensorflow as tf
import keras
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
import sklearn

dataList = {}
def getEnum(column):
    result = {}

    for i in column:
        item = result.get(i, 0)

        result[i] = item+1

    print(list(result.keys()))
    return list(result.keys())

def indexData(column, list):
    newColumn = []

    for i in column:
        # print(i)
        item = list.index(i)
        newColumn.append(item)

    print(newColumn)


# print(result.keys())
    return newColumn


def convertStringsToNumbersOLD(data, columns):

    for i in columns:
        print(i)
        if (i == "salary_minimum") | (i == "salary_maximum") | (i == "num_vacancies"):
            continue

        dataList[i] = getEnum(data[i])

    print("----------------------------------------------------")
    # print(dataList)

    for i in columns:
        if (i == "salary_minimum") | (i == "salary_maximum") | (i == "num_vacancies"):
            # data[i] = data[i]
            pass
        else:
            newColumn = indexData(data[i], dataList[i])
            data[i] = newColumn

    # print(newData.keys())
    return data


def convertStringsToNumbers(data, columns):
    # creating labelEncoder
    le = preprocessing.LabelEncoder()

    for i in columns:
        if (i == "salary_minimum") | (i == "salary_maximum") | (i == "num_vacancies"):
            continue

        data[i] = le.fit_transform(data[i])

    print(data)
    return  data


data = pd.read_csv("Wuzzuf_Job_Posts_Sample.csv", sep=",")

# print first 5 rows
# print(data.head())
columns = ["city", "job_title", "salary_minimum", "salary_maximum", "num_vacancies", "career_level", "experience_years",
           "job_category1", "job_category2", "job_category3","job_industry1"]
data = data[columns]

getEnum(data["job_category1"])
getEnum(data["job_category2"])
getEnum(data["job_category3"])
# data = convertStringsToNumbers(data, columns)

# data = pd.DataFrame(data.items())
# print(data.head())
#
#
# predict = "salary_minimum"
#
# x = np.array(data.drop([predict], 1))
# y = np.array(data[predict])
#
# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
#
# linear = linear_model.LinearRegression()
# linear.fit(x_train, y_train)
#
# acc = linear.score(x_test, y_test)
# print("accc: ", acc)

# print("cef: ", linear.coef_)
# print("interc: ", linear.intercept_)

# predicts = linear.predict(x_test)