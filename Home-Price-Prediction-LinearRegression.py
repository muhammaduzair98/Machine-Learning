import pandas as pd
import numpy as np
from sklearn import linear_model
import math


#dataset

df = pd.read_csv("/Users/eapple/Local Disk/homepricesheet.csv")
df

df.bedrooms.median()

df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())
df

reg = model = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)


reg.coef_


reg.intercept_

reg.predict([[3000,4,1]])

import matplotlib.pyplot as plt
plt.plot(df.price)

plt.show()

