from datetime import *
import pandas as pd
import numpy as np
import datetime
import time
import pyfolio as pf
#import empyrical  as ep
#import matplotlib.pyplot as plt
import math
import pytz
#raw=w.wsd("510050.SH", "close", "2015-04-16", "2016-11-15", "")
#df2=raw.Data


df=pd.read_csv(r'C:\Users\maoheng\Desktop\高诗涛\netvalue.csv')
#etf=pd.read_csv(r'\Users\hmy\Desktop\50etf.csv')

#df['netvalue']=df['totalAssets']/df['initialAssets']
#df['ret']=df['totalAssets']/df['totalAssets'].shift(1)-1
#df.loc[0,'ret']=df['totalAssets'][0]/df['initialAssets'][0]-1
data=pd.DataFrame()
data['Date']=df.ix[:,0]
data['ret']=df['netvalueReturn']

for i in range(len(data)):
  data.loc[i,'newdate']=datetime.datetime.strptime(data['Date'][i], "%Y/%m/%d %H:%M:%S 000")

for i in range(len(data)): 
  data.loc[i,'newdate']=data['newdate'][i].date()

data.index=data['newdate']
del(data['newdate'])
del(data['Date'])
data2=pd.Series(data)
data2=data.iloc[:,0]
data2[0]=0
data2.index.tz=pytz.timezone('Asia/Shanghai')
etfdata=pd.Series()
etfdata=df['benchmarkReturn']
etfdata[0]=0
etfdata.index=data2.index
etfdata.index.tz=pytz.timezone('Asia/Shanghai')
pf.create_returns_tear_sheet(data2,benchmark_rets=etfdata)