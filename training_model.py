import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# read the data from a csv file
music_data = pd.read_csv('weather.csv') 

# CLEAN THE TRAINING AND PREDICTING DATA
x = music_data.drop(columns=['output'])
y = music_data['output']

# create model
model = DecisionTreeClassifier()
model.fit(x,y)

# make predictions
trained_model = joblib.dump(model,'trained_model.joblib')
