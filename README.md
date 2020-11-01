# Weather_Predictor using Machine Learning  [REAL TIME]

This is a predictor which predicts weather by reading the given input data

and recongnising patterns of the data and making predictions on gven that

## Steps
**To directly use .open** *weather_predictor.py file*

**To make diff model follow the steps**

> **open *training_model.py* and make changes to the model.

> **after training. dump the model

> **and load it to the *weather_predictor.py* file by

```python
joblib.load('trained_model.joblib')
```

## Modules Used
> **Pandas  [pip install pandas]**

> **requests [pip install requests]**

> **Sklearn [pip install sklearn]**

> **Joblib [pip install joblib]**

## <a href='https://openweathermap.org/api'>Open Weather API </a> was used to fetch data.
 
