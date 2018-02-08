#!/usr/bin/python
# -*- coding: utf-8 -*-
import os  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import psycopg2
import sqlalchemy
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.formula.api as smf

engine = sqlalchemy.create_engine("postgresql+psycopg2://smyyeozturk:ozturk.1928@localhost:5432/fiyattahmin")

table_name = 'evtahmin_fiyattahmin'

data = pd.read_sql_table(table_name, engine, columns=['metreKare','odaSayisi','fiyat']) 

X = data[['metreKare','odaSayisi']]
Y = data['fiyat']
df1 = pd.DataFrame(X,columns=['metreKare','odaSayisi'])
df1['fiyat']= pd.Series(Y)


model = smf.ols(formula='fiyat ~ metreKare + odaSayisi', data=df1)
results_formula = model.fit()

x_surf, y_surf = np.meshgrid(np.linspace(df1.metreKare.min(), df1.metreKare.max()),np.linspace(df1.odaSayisi.min(), df1.odaSayisi.max()))
##ravel --> düzleştirilmiş bir veriyi ndarray olarak döndürür.
onlyX = pd.DataFrame({'metreKare': x_surf.ravel(), 'odaSayisi': y_surf.ravel()})
fittedY=results_formula.predict(exog=onlyX)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df1['metreKare'],df1['odaSayisi'],df1['fiyat'],c='blue', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.values.reshape(x_surf.shape), color='None', alpha=0.01)
ax.set_xlabel('Metre Kare')
ax.set_ylabel('Oda Sayisi')
ax.set_zlabel('Fiyat')
mKare = int (input("Metre Kare Giriniz :"))
oSayisi = int(input("Oda Sayisini Giriniz:"))
x_new = [[mKare,oSayisi]]
print x_new
df1_new= pd.DataFrame(x_new,columns=['metreKare','odaSayisi'])
print results_formula.predict(df1_new)


