import tensorflow as tf
import keras
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
import sklearn

dataList = {}

data = pd.read_csv("Wuzzuf_Job_Posts_Sample.csv", sep=",")

columns = ["city", "job_title", "salary_minimum", "salary_maximum", "num_vacancies", "career_level", "experience_years",
           "job_category1", "job_category2", "job_category3", "job_industry1", "job_industry2", "job_industry3"]
data = data[columns]


# Get all available values
def getEnum(columnName):
    result = {}
    for i in data[columnName]:
        item = result.get(i, 0)
        result[i] = item + 1

    return list(result.keys())


def removeSpaces(columnName):
    result = []
    for i in range(len(data[columnName])):
        result.append(data[columnName][i].replace(" ", ""))

    data[columnName] = result


# represent list in binary
def getBinaryRepresentation(enum, columnName1, columnName2, columnName3):
    result = []
    for j in range(len(data[columnName1])):
        item = ""
        for i in enum:
            if (i == data[columnName1][j]) | (i == data[columnName2][j]) | (i == data[columnName3][j]):
                item += "1"
            else:
                item += "0"
        # print("item: ", item)
        result.append(item)
    print("result len: ", len(result))
    return result


def convertStringsToNumbers():
    # creating labelEncoder
    le = preprocessing.LabelEncoder()

    for i in newColumns:
        if (i == "salary_minimum") | (i == "salary_maximum") | (i == "num_vacancies") | (i == "job_industry")\
                | (i == "job_category"):
            continue

        data[i] = le.fit_transform(data[i])


# Cities data before processing
# enumCity = getEnum("city")
# print("enumCity: ", enumCity)
# print("enumCity len: ", len(enumCity))

# Cities data remove white spaces
removeSpaces("city")
# enumCity = getEnum("city")
# print("enumCity: ", enumCity)
# print("enumCity len: ", len(enumCity))

# Get all available values for job_category
# job_category1, job_category2, job_category3 All has the same values "By testing"
removeSpaces("job_category1")
enumCategory = getEnum("job_category1")
print("enumCategory len: ", len(enumCategory))
data["job_category"] = getBinaryRepresentation(enumCategory, "job_category1", "job_category2", "job_category3")


# Get all available values for job_industry
removeSpaces("job_industry1")
removeSpaces("job_industry2")
enumIndustry = getEnum("job_industry1")
enumIndustry2 = getEnum("job_industry2")
print("enumIndustry len: ", len(enumIndustry))

#  merge job_industry1 with job_industry2
for i in enumIndustry2:
    found = False
    for j in enumIndustry:
        if j == i:
            found = True

    if not found:
        print("New: ", i)
        enumIndustry.append(i)
print("enumIndustry len: ", len(enumIndustry))


data["job_industry"] = getBinaryRepresentation(enumIndustry, "job_industry1", "job_industry2", "job_industry3")


newColumns = ["city", "job_title", "salary_minimum", "salary_maximum", "num_vacancies", "career_level",
              "experience_years", "job_category", "job_industry"]

data = data[newColumns]

convertStringsToNumbers()

print(data.head())

# predict = "salary_minimum"
# x = np.array(data.drop([predict], 1))
# y = np.array(data[predict])
# x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
#
# linear = linear_model.LinearRegression()
# linear.fit(x_train, y_train)
#
# acc = linear.score(x_test, y_test)
# print("accc: ", acc)







