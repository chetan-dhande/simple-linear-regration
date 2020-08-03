# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:59:00 2020

@author: Chetan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

emp =pd.read_csv("C:\\Users\\ADMIN\\Desktop\\chetan\\assignment\\simple liniar regration\\Salary_Data.csv")
emp.columns

plt.hist(emp['YearsExperience'])
plt.hist(emp['Salary'])
plt.boxplot(emp['YearsExperience'])
plt.boxplot(emp['Salary'])
plt.plot(emp['YearsExperience'],emp['Salary'],"ro" );plt.xlabel("YearsExperience");plt.ylabel("Salary")

import statsmodels.formula.api as smf
model1 = smf.ols("Salary~YearsExperience",data=emp).fit()
type(model1)
model1.params
model1.summary() 

model1.conf_int(0.05)
pred = model1.predict(emp)

plt.plot(emp['YearsExperience'],emp['Salary'],"ro" );
plt.plot(emp['YearsExperience'],pred,color='black');plt.xlabel('YearsExperience');plt.ylabel('Salary')

