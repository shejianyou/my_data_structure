# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:53:51 2019

@author: 23909
"""
#导入apple公司股票数据
import pandas_datareader as pdr
import datetime
apple = pdr.get_data_yahoo('AAPL',
                           start=datetime.datetime(1980,1,1),
                           end=datetime.datetime(2019,12,29))
#导入numpy和pandas
import numpy as np
import pandas as pd

#选取调整的收盘价
adj_close_px = apple['Adj Close']
#计算移动均值
moving_avg = adj_close_px.rolling(window=40).mean()
#查看后十项结果
print(moving_avg[-10:])

#导入matplotlib
import matplotlib.pyplot as plt
#短期的移动窗口
apple['42'] = adj_close_px.rolling(window=40).mean()
#长期的移动窗口
apple['252'] = adj_close_px.rolling(window=252).mean()
#绘制调整的收盘价，同时包含短期和长期的移动窗口均值
apple[['Adj Close','42','252']].plot(figsize=(15,20))
#图片另存为
plt.savefig('E:\stock\移动窗口',dpi=400,bbox_inches='tight')
plt.show()

#移动窗口
#定义最小周期
min_periods = 75
#计算移动波动率
daily_pct_change = adj_close_px.pct_change()
vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)
#绘制波动率曲线
vol.plot(figsize=(10,8))
#图片另存为
plt.savefig('E:\stock\波动率移动窗口',dpi=400,bbox_inches='tight')
plt.show()


























