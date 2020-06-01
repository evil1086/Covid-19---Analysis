# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:28:00 2020

@author: user
"""
#import all the lib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#imporint dataset from the location
age_wise_data = pd.read_csv('AgeGroupDetails.csv')
india_dataset = pd.read_csv('covid_19_india.csv')


#dataset creaion
region_wise = pd.DataFrame(india_dataset)



#Slicing for age_wise_data
age_group = age_wise_data.iloc[:,1]
total_count = age_wise_data.iloc[:,2]


#Ploting for age_wise_data
plt.bar(age_group, total_count, label='Covid19-India Age wise Dataset(APR end)')
plt.ylabel('Count in the Numbers')
plt.xlabel('Age matrix')
plt.grid()
#plt.legend()
plt.show()
plt.close()
#slicing for india_dataset
#region = india_dataset.iloc[:,2]
print (region_wise.groupby('State/UnionTerritory')['Confirmed', 'ConfirmedIndianNational', 'ConfirmedForeignNational', 'Cured', 'Deaths'].plot(kind='barh'))

plt.close()
#region_wise['State/UnionTerritory'] = [ region_wise["State/UnionTerritory"][i] == region_wise["State/UnionTerritory"][i] for i in range(len(region_wise["State/UnionTerritory"]))]

