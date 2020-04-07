import pandas as pd
from sklearn import preprocessing
from classifiers import linearRegressionClassifier, gaussianNBClassifier, knnClassifier
from cities import filterCities, egGov
from utilities import getEnum, removeSpaces, addBinaryAsFeaturesFromList, filterExperienceYears

dataList = {}

data = pd.read_csv("Wuzzuf_Job_Posts_Sample.csv", sep=",")

# columns = ["city", "job_title", "salary_minimum", "salary_maximum", "num_vacancies", "career_level",
#            "experience_years", "job_category1", "job_category2", "job_category3", "job_industry1", "job_industry2",
#            "job_industry3"]
# data = data[columns]


# represent list in binary
def addBinaryAsFeatures(enum, columnName1, columnName2, columnName3):
    for i in enum:
        newFeature = []
        for j in range(len(data[columnName1])):
            if (i == data[columnName1][j]) | (i == data[columnName2][j]) | (i == data[columnName3][j]):
                newFeature.append(1)
            else:
                newFeature.append(0)
        # print("result len: ", newFeature)
        data[i] = newFeature
    # return result


def convertStringsToNumbers():
    # creating labelEncoder
    le = preprocessing.LabelEncoder()

    for i in newColumns:
        if (i == "job_title") | (i == "career_level"):
            data[i] = le.fit_transform(data[i])


data["experience_years"] = filterExperienceYears(data["experience_years"])


data["city"] = filterCities(data["city"])
newCitiesDict = addBinaryAsFeaturesFromList(egGov, data["city"])
for i in newCitiesDict:
    data[i] = newCitiesDict[i]

# Get all available values for job_category
# job_category1, job_category2, job_category3 All has the same values "By testing"
removeSpaces(data["job_category1"])
enumCategory = getEnum(data["job_category1"])
print("enumCategory len: ", len(enumCategory))
addBinaryAsFeatures(enumCategory, "job_category1", "job_category2", "job_category3")


newColumns = ["salary_minimum", "num_vacancies", "career_level", "experience_years"] + enumCategory + egGov

data = data[newColumns]

convertStringsToNumbers()

print(data.head())
linearRegressionClassifier(data)
gaussianNBClassifier(data)
knnClassifier(data)



