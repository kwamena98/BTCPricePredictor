import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle


model=LinearRegression()

df=pd.read_csv("AllCryptoTrend.csv",index_col=False)

BTC=df[df.Type=="Bitcoin USD"]

x=BTC.drop(columns=['Type','Date','Adj Close','Close'])
print(x.columns)
y=BTC['Close']


model.fit(x,y)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
