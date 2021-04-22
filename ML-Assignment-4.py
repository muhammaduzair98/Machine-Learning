import pandas as pd
import numpy as np

from sklearn.neighbors import LocalOutlierFactor

from google.colab import drive
drive.mount('/content/drive')

fpath = "/content/drive/My Drive/data/Mall_customers.csv"
dataset = pd.read_csv(fpath) #reading path
dataset  #printing

aIncome  = data.iloc[:, 3].values
aIncome #printing Annual Income
aMedium = np.median(aIncome)
print('Global Median ', aMedian)

aCutoff = aMedian * 2 # k [1, 4], k = 2
aLower, aUpper = aMedian - aCutoff, aMedian + aCutoff
print('Annual Lower Points and Annual Upper Point', aLower, aUpper)

for income in aIncome:
  if (income < aLower or income > Upper):
    print(income)

spendingScore = corpus.iloc[:, 4].values

spendingMedian = np.median(spendingScore)

spendingCutoff = spendingMedian * 2  

spendingLower, spendingUpper = spendingMedian - spendingCutoff, spendingMedian + spendingCutoff

print('spendingLower & spendingUpper', spendingLower, spendingUpper)

for spending in spendingScore:
  if spending < spendingLower or spending > spendingUpper:
    print(spending)

vdata = dataset.iloc[:, 2:5].values

print(vdata)

LOF = LocalOutlierFactor(n_neighbors = 2)

result = LOF.fit_predict(data) #Predicting Values LOF

print (result)