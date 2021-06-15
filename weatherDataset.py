import numpy as np
import pandas as pd
data = pd.read_csv(r"E:\1. Weather Data.csv")
print(data)
print(data.head()) #It shows the first n rows in the data (by default N=5)
print(data.shape) #total no. of rows and no. of columns of the dataframe
print(data.index)
print(data.columns)
print(data.dtypes)
print(data['Weather'].unique()) # It shows all unique values
print(data.nunique())
print(data.count())
print(data['Weather'].value_counts())# It shows all the unique values with their column
print(data.info())
print(data.head(2))
print(data.nunique())
print(data['Wind Speed_km/h'].nunique())
print(data['Wind Speed_km/h'].unique())
print(data.Weather.value_counts())
print(data[data.Weather == 'Clear']) # filtering
print(data.groupby('Weather').get_group('Clear'))
print(data[data['Wind Speed_km/h'] == 4])#number of times when "Wind speed was exactly 4 km/h"
print(data.isnull().sum())
print(data.notnull().sum())
print(data.rename(columns= {'Weather':'Weather Condition'}, inplace = True))
print(data.head())
print(data.Visibility_km.mean())
print(data.Press_kPa.std()) #Standard Deviation of 'Pressure'in this data
print(data['Rel Hum_%'].var())
print(data['Weather Condition'].value_counts())
print(data[data['Weather Condition'] == 'Snow'])
print(data[data['Weather Condition'].str.contains('Snow')].tail(50))
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])
print(data.groupby('Weather Condition').mean())
print(data.groupby('Weather Condition').min())
print(data.groupby('Weather Condition').max())
print(data[data['Weather Condition'] == 'Fog'])
print(data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km' ]> 40)].head(50))
print(data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km' ]> 40)].tail(50))
print(data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)])
