import pandas as pd
import os

import seaborn 
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB


seaborn.set()



# loading cleaned data
cleaned_files = [file for file in os.listdir("data/cleaned-data/")]

df = pd.DataFrame()
for file in cleaned_files:
    data = pd.read_csv("data/cleaned-data/" + file)
    df = pd.concat([df, data])

# Monthly DataFrames
num_of_years = df["YEAR"].max() - df["YEAR"].min() + 1
data = data[data["YEAR"] >= 2021]
data = data[data["YEAR"] <= 2022]

df = data.dropna()

neighbor = preprocessing.LabelEncoder()
block = preprocessing.LabelEncoder()

dfc = df.copy(deep=True)
dfc["NEIGHBOURHOOD"] = dfc["NEIGHBOURHOOD"].apply(lambda x: str(x))

neighbor.fit(dfc["NEIGHBOURHOOD"])
dfc["NEIGHBOURHOOD"] = neighbor.transform(dfc["NEIGHBOURHOOD"])


X = dfc[["MONTH", "NEIGHBOURHOOD", "LAT", "LON"]]
y = dfc["MONTH"]

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.80)


#bayes
bayes_model = GaussianNB()
bayes_model.fit(X_train, y_train)

print(bayes_model.score(X_train, y_train))
print(bayes_model.score(X_valid, y_valid))


#decision tree

model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

print(model.score(X_train, y_train))
print(model.score(X_valid, y_valid))

#forest

model = RandomForestClassifier(n_estimators=9,
                               max_depth=5)
model.fit(X_train, y_train)

print(model.score(X_train, y_train))
print(model.score(X_valid, y_valid))



