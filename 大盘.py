# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:55:55 2019

@author: 23909
"""

import datetime
import pandas as pd
import pandas_datareader.data as web
start = datetime.datetime(2019,11,25)
end = datetime.datetime(2019,11,29)
df = web.DataReader('AAPL')
print(df)

import datetime
import pandas as pd
import pandas_datareader.data as web
start = datetime.datetime(2019,11,25)
end = datetime.datetime(2019,11,29)
a_df = web.DataReader('.INX')
print(a_df)
