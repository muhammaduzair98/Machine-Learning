import numpy as np
import pandas as pd
from sklearn import linear_model
import math 


#DatasetImport

df = pd.read_csv("/Users/eapple/Desktop/ml.csv")
df


reg = model = linear_model.LinearRegression()
reg.fit(df[['assignment','quiz','S1', 'S2', 'final','project']],df.score)

reg.coef_

reg.intercept_

pred_result = reg.predict([[6.25,3.75,5.76,7.5,24.11,9]])

print(pred_result)

