# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:48:29 2019

@author: 23909
"""
#导入apple公司股票数据
import pandas_datareader as pdr
import datetime
aapl = pdr.get_data_yahoo(
        'AAPL',
        start=datetime.datetime(1980,1,1),
        end=datetime.datetime(2019,12,29))
print(aapl)
aapl.to_csv(r'E:\stock\apple.csv',index=True)
information = aapl.info()

#导入numpy和pandas
import numpy as np
import pandas as pd
#将aapl数据框中'Adj Close'列数据赋值给变量'daily_close'
daily_close = aapl[['Adj Close']]
#计算每日收益率
daily_pct_change = daily_close.pct_change()
#用0填补缺失值NA
daily_pct_change.fillna(0, inplace=True)
#查看每日收益率的前几行
print(daily_pct_change.head())
#计算每日对数收益率
daily_log_returns = np.log(daily_close.pct_change()+1)
#查看每日对数收益率的前几行
print(daily_log_returns.head())
#按营业月对'aapl'数据进行重采样，取每月最后一项
monthly = aapl.resample('BM').apply(lambda x: x[-1])
#计算每月的百分比变化，并输出前几行
print(monthly.pct_change().head())
#按季度对'aapl'数据进行重采样，将均值改为每季度的数值
quarter = aapl.resample('3M').mean()
#计算每季度的百分比变化，并输出前几行
print(quarter.pct_change().head())
#每日收益率
daily_pct_change = daily_close / daily_close.shift(1) - 1
#输出'daily_pct_change'的前几行
print(daily_pct_change.head())
#导入matplotlib
import matplotlib.pyplot as plt
#绘制直方图
daily_pct_change.hist(bins=50)
plt.savefig(r'E:\stock\return_hist',dpi=400,bbox_inches='tight')
plt.show()

#输出daily_pct_change的统计摘要
print(daily_pct_change.describe())
#计算累积日收益率
cum_daily_return = (1 + daily_pct_change).cumprod()
#输出'cum_daily_return'
print(cum_daily_return)
#绘制累积日收益率曲线
cum_daily_return.plot(figsize=(12,8))
plt.savefig(r'E:\stock\cum_daily_return',dpi=400,bbox_inches='tight')
plt.title('cum_daily_return')
plt.show()
#将累积日回报率转换成累积月回报率
cum_monthly_return = cum_daily_return.resample("M").mean()
#输出'cum_monthly_return'的前几行
#print(cum_monthly_return.head())
print(cum_monthly_return)

#获取Apple、Microsoft、IBM和Google的股票数据，并将它们合并在一个大的数据框中
import pandas_datareader as pdr
import datetime
import yfinance

def get(tickers, startdate, enddate):
    def data(ticker):
        return (pdr.get_data_yahoo(ticker, start=startdate,end=enddate))
    datas = map(data, tickers)
    return (pd.concat(datas, keys=tickers,names=['Ticker','Date']))
tickers = ['AAPL','MSFT','IBM','GOOG']
all_data = get(tickers, datetime.datetime(1980,1,1),datetime.datetime(2019,12,29))
print(all_data.head())
print(all_data)
#选取'Adj Close'这一列并变换数据框
daily_close_px = all_data[['Adj Close']].reset_index().pivot('Date','Ticker','Adj Close')
#对'daily_close_px'计算每日百分比变化
daily_pct_change = daily_close_px.pct_change()
#绘制分布直方图
daily_pct_change.hist(bins=50,sharex=True,figsize=(12,8))
#将绘图效果另存为
plt.savefig(r'E:\all_data',dpi=400,bbox_inches='tight')
#显示绘图结果
plt.show()
#对'daily_pct_change'数据绘制散点矩阵图
pd.plotting.scatter_matrix(daily_pct_change,diagonal='kde',alpha=0.1,figsize=(12,12))
#显示绘图结果
plt.show()

#定义最小周期
min_periods = 75
#计算波动率
vol = daily_pct_change.rolling(min_periods).std()*np.sqrt(min_periods)
#绘制波动率曲线
vol.plot(figsize=(10,8))
#图片另存为
plt.savefig(r'E:\stock\移动波动率',dpi=400,bbox_inches='tight')
#显示结果
plt.show()












































