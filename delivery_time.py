# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:54:41 2020

@author: Chetan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

time = pd.read_csv("C:\\Users\\ADMIN\\Desktop\\chetan\\assignment\\simple liniar regration\\delivery_time.csv")

time.corr()
time.columns

plt.hist(time["Delivery"])
plt.hist(time["Sorting"])
plt.boxplot(time['Delivery'])
plt.boxplot(time['Sorting'])
plt.plot(time['Delivery'],time['Sorting'],"ro" );plt.xlabel("Delivery Time");plt.ylabel("Sorting Time")

import statsmodels.formula.api as smf
model1 = smf.ols("Sorting~Delivery",data=time).fit()
type(model1)
model1.params
model1.summary()

model1.conf_int(0.05)
pred = model1.predict(time)
print(model1.conf_int(0.05))


plt.scatter(x=time['Delivery'], y=time['Sorting'], color='red');
plt.plot(time['Delivery'],pred,color='black');plt.xlabel('Delivery Time');plt.ylabel('Sorting Time')

