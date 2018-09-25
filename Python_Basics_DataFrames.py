i# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 20:05:19 2018

@author: Aveedibya Dey
"""
import pandas as pd

#You may need to update this path
DataFile = "GroceryData.csv"
 
df1 = pd.read_csv(DataFile)

#OR - Define a Datframe in-line
x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})

#---------------------------------------
#Data Frame commands
#---------------------------------------

df1.columns   #View Column names
df1[1:2]        #View certain row range, Ex. Start from 1, stop before 2  
df1.dtypes      #Show column types
df1.head()      #Show top few rows
df1.tail(3)     #Show bottom 3 rows
df1.values      #Show values


#Select multiple columns from dataframe
df1[['Customer ID', 'Purchase Qty']] #Note double square brackets

#Select subset of rows for specific columns
df1[['Customer ID', 'Purchase Qty']][1:5]

#Transforming columns, or re-assigning
df1[['Customer ID', 'Purchase Qty']] = df2[['Cust ID', 'Items Bought']]

#Select rows with a filter
df1[df1['Purchase Qty']>25]
#Note: Only df1['Purchase Qty']>25 shows a bolean True/False for the condition

#Multiple conditions work too
df1[(df1['Purchase Qty']>10) & (df1['Category']=='Cosmetics')]
#For OR, use '|' ---> without apostrophe, straight vertical line

#Copy Dataframe
df2 = df1
df3 = df1


#Inner Join 
df_Joined = df2.set_index('Customer ID').join(df3.set_index('Customer ID'), lsuffix='_l')

#--------------------------------
#Source: https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html
#COMPARE WITH SQL
#--------------------------------

#Select distinct(Category) from Table
df1[['Category']].drop_duplicates()

#SELECT * FROM TABLE WHERE CATEGORY='Cosmetics' LIMIT 5;
df1[df1['Category']=='Cosmetics'].head(5)

#SELECT count(Customer ID) from TABLE GROUPBY Category
df1.groupby('Category')['Customer ID'].count()

import numpy as np #Import Numpy module for aggregation
#SELECT AVG(Purchase_Amt), SUM(PURCHASE_QTY) FROM TABLE GROUPBY Category
df1.groupby('Category').agg({'Purchase Amt(USD)':np.mean,'Purchase Qty':np.sum})

#Try combining few queries from above
df1[(df1['Purchase Qty']>10)].groupby('Category')['Customer ID'].count()

#Define two new subset dataframes
df_Cosmetics = df1[df1['Category']=='Cosmetics']
df_Produce = df1[df1['Category']=='Produce']

#SELECT * from df_Cosmetics INNER JOIN df_Produce 
#on df_Cosmetics.Purchase_Qty = df_Produce.Purchase_Qty 
df_INNER_JOINED = pd.merge(df_Cosmetics, df_Produce, on='Purchase Qty')

#Similar to above - LEFT JOIN
df_LEFT_JOINED = pd.merge(df_Cosmetics, df_Produce, on='Purchase Qty', how='left')

#Values how = 'left', how = 'right', how = 'outer'

#SELECT * from df_Cosmetics UNION df_Produce
df_UNION = pd.concat([df_Cosmetics, df_Produce]) #Don't forget [] inside ()


