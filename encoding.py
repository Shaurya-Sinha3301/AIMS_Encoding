import numpy as np 
import pandas as pd
#one hot encoding
dataset=pd.read_csv('Data.csv')
countries = dataset['Country'].unique()
countryDict={country: np.eye(len(countries))[i] for i, country in enumerate(countries)}
oneHotCoutries=np.array([countryDict[country] for country in dataset['Country']])
for i, country in enumerate(countries):
    dataset[country]=oneHotCoutries[:,i]

dataset.drop('Country',axis=1,inplace=True)

print(dataset.head())

#ordinal
data2=pd.read_csv('grades.csv')
gradeEncoding={'A': 3, 'B': 2, 'C': 1}
data2['Ordinal_Grades']=data2['Grade'].map(gradeEncoding)

print(data2)