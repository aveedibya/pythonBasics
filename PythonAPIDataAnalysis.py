#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:19:40 2019
@author: Aveedibya Dey
"""
#Libraries needed to read API data, and parse json data
import urllib.request, json 

#Read an API JSON data
with urllib.request.urlopen("https://callgenapi.herokuapp.com/interval_aggregate") as url:
    print(url)
    print("-------")
    jsoncalldata = json.loads(url.read().decode())
    print(jsoncalldata)
    
#Analyze the json object
#...
type(jsoncalldata)
#...
jsoncalldata.keys()
#...
jsoncalldata['metahead']
#...
type(jsoncalldata['metahead'])
#...
jsoncalldata['metahead'].keys()
#...
jsoncalldata['metahead']['BAU']
#...
jsoncalldata['data']
#...
type(jsoncalldata['data'])
#...

#JSON Data to DataFrame
#-----
import pandas as pd
df = pd.DataFrame(jsoncalldata['data'])
df = df.transpose()

#Convert interval to datetime format
df['interval'] = pd.to_datetime(df['interval'])

#Extract Date/Time attributes from a datetime column
df['interval'].dt.minute
df['hour'] = df['interval'].dt.hour

#Aggregation
#-----
import numpy as np

#Sum the calls
df.groupby('hour')['call_count'].agg({'call_count_sum': np.sum})

#Plotting
#-----
#Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html
#-----
#import matplotlib.pyplot as plt
#x = df['hour'].drop_duplicates()
#y = df.groupby('hour')['call_count'].agg({'call_count_sum': np.sum})['call_count_sum']
#
#plt.bar(x, y)
#plt.xticks(x, x)
#plt.show()

aggdf = df.groupby('hour')['call_count'].agg({'call_count_sum': np.sum})
aggdf.plot.bar(rot=0)


#Seaborn Plots
#------
import seaborn as sns
sns.set()

#Replot now, better styling?
aggdf.plot.bar(rot=0)
#------
#Reference: https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
#------
aggdf.plot.bar(rot=0, figsize=(10,10))





















