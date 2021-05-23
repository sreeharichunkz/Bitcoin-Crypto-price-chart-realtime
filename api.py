#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pycoingecko')
get_ipython().system('pip install plotly')
get_ipython().system('pip install mplfinance')


# In[6]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc


# In[10]:


dict_={'a':[11,21,31], 'b':[12,22,32]}


# In[16]:


df=pd.DataFrame(dict_)
type(df)
df
dict_


# In[14]:


df.head()


# In[15]:


df.mean()


# In this lab, we will be using the <a href=https://www.coingecko.com/en/api?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01>CoinGecko API to create one of these candlestick graphs for Bitcoin. We will use the API to get the price data for 30 days with 24 observation per day, 1 per hour. We will find the max, min, open, and close price per day meaning we will have 30 candlesticks and use that to generate the candlestick graph. Although we are using the CoinGecko API we will use a Python client/wrapper for the API called <a href=https://github.com/man-c/pycoingecko?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01>PyCoinGecko. PyCoinGecko will make performing the requests easy and it will deal with the enpoint targeting.

# In[17]:


cg = CoinGeckoAPI()
bitcoin_data =cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='inr', days=30)


# In[18]:


type(bitcoin_data )


# In[19]:


bitcoin_data


# In[21]:


bitcoin_price_data=bitcoin_data['prices']
bitcoin_price_data[0:5]


# In[37]:


data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])


# In[23]:


data


# In[38]:


data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')


# In[39]:


candlestick_data = data.groupby(data.Date.dt.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})


# In[40]:


fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()


# In[ ]:




