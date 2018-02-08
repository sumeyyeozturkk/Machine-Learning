import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine("postgresql+psycopg2://smyyeozturk:ozturk.1928@localhost:5432/fiyattahmin")

table_name = 'evtahmin_fiyattahmin'

data = pd.read_sql_table(table_name, engine)

x = data["metreKare"]
y = data["fiyat"]


m,b = np.polyfit(x,y,1)

a = np.arange(300)

plt.scatter(x,y)
plt.plot(m*a+b)

z = int(input("Metrekare Girin: "))
tahmin = m*z+b
print int(tahmin)

plt.scatter(z,tahmin,c = "red", marker = ">")
plt.show()

