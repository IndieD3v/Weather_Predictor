import requests
from sklearn.tree import DecisionTreeClassifier
import joblib

# key and city name
api_key = 'API KEY HERE'
city_name = input("Enter City Name: ")

# main url
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

res = requests.get(url)
data = res.json()

# fetching all necessary data 
temprature = data['main']['temp']
humidity = data['main']['humidity']
wind_speed = data['wind']['speed']

print(f'\nTemprature > {temprature} K')
print(f'Humidity > {humidity}')
print(f'Wind Speed > {wind_speed}\n')

# Loading the TRAINED model 
trained_model = joblib.load('trained_model.joblib')

# give data to predict
predict = trained_model.predict([[
    temprature,
    humidity,
    wind_speed]]
    )

print(f'Today is a {predict} day in {city_name}\n')
