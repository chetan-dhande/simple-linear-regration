# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:32:47 2020

@author: Chetan
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf 
from ml_metrics import rmse

calories1 = pd.read_csv('C:\\Users\\ADMIN\\Desktop\\chetan\\assignment\\simple liniar regration\\calories_consumed.csv')
calories1.columns
plt.hist(calories1['Weight'])
plt.boxplot(calories1['Weight'])
plt.plot(calories1['Calories'],calories1['Weight'],"ro");
plt.xlabel("Calories)");plt.ylabel("Weight")
plt.hist(calories1["Calories"])
plt.boxplot(calories1["Calories"])

calories1.corr()
import statsmodels.formula.api as smf
model=smf.ols("Weight~Calories",data=calories1).fit()
type(model)
model.params
model.summary()

model.conf_int(0.05)
pred = model.predict(calories1)
print(model.conf_int(0.05))


plt.scatter(x=calories1['Calories'],y=calories1['Weight'],color='red');
plt.plot(calories1['Calories'],pred,color='black');plt.xlabel('Weight');plt.ylabel('Calories')
