# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:23:40 2019

@author: Ritvik.Tiwari
"""

# Crime-Literacy
import pandas as pd 
import matplotlib.pyplpot as plt
import numpy as np

cl= pd.read_csv("c:/user/ritvik.tiwari/desktop/Crime_Literacy.csv")
X = cl['Total_Literates']
y = cl['Total_Crimes']
from sklearn import linear_model
import statsmodel.api as sm
model=sm.OLS(y,X).fit()
model.summary()

#Generated linear fit
slope,intercept, r_value, p_value,std_err = stats.lineregress(x,y)
line = slope* + intercept

plt.plot(x,y,'o'x,line)
pylab.title('Crime Literate')
pylab.xlabel('Total_Literate')
pylab.ylabel('Total_Crimes')
ax = plt.gca()
fig =plt.gcf()
plot_mpl(fig, filename= 'linear regression')

plt.show()