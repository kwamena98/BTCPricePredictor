import pandas as pd 
from sklearn.linear_model import LinearRegression
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
