# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:25:26 2020

@author: Chetan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

emp =pd.read_csv("C:\\Users\\ADMIN\\Desktop\\chetan\\assignment\\simple liniar regration\\emp_data.csv")
emp.columns

plt.hist(emp['Salary'])
plt.hist(emp['Churn'])
plt.boxplot(emp['Salary'])
plt.boxplot(emp['Churn'])
plt.plot(emp['Salary'],emp['Churn'],"ro" );plt.xlabel("Salary_hike");plt.ylabel("Churn_out_rate")

import statsmodels.formula.api as smf
model1 = smf.ols("Churn~Salary",data=emp).fit()
type(model1)
model1.params
model1.summary() 

model1.conf_int(0.05)
pred = model1.predict(emp)

plt.scatter(x=emp['Salary'], y=emp['Churn'], color='red');
plt.plot(emp['Salary'],pred,color='black');plt.xlabel('salary');plt.ylabel('churn')

