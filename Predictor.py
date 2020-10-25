import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Reading the csv data
data = pd.read_csv('wheather.csv')

# Cleaning out the data
x = data.drop(columns=['outlook'])
y = data['outlook']

# Making Model
model = DecisionTreeClassifier()
# giving the input and output data
model.fit(x,y)

# making predictions of given data
predictions = model.predict([[22,20]])
print(predictions)