"""
pandas : pip install pandas

use  : 
1. data cleaning  : missing value , data type
2. data manupulation : sort , filter , merge , join
3. data analysis : univarite analysis , bivariate analysis , multivariate analysis
4. sorting  , merge  , join, filter , groupby

2. 2 ways  data : 
1. seris : 1 dementional  data structure .
2. dataframe : 2 dementional  data structure .

"""
import  pandas as pd
import numpy as np
# seris : 1 dementional  data structure .

"""a= pd.Series([10,20,30,40,50,60,70,80,90,100])
print(a)

b=pd.Series([90,97,91,92,94],index=["ram","sita","raj","dhan","bhagwat"])
print(b)

c= pd.Series({"ram":90,"sita":97,"raj":91,"dhan":92,"bhagwat":94})
print(c)

d= pd.Series([12,34,56,78,np.nan],index=[1,2,3,4,5])
print(d)

e= pd.Series(["ram",12,45,67,89,90.89],index=[1,2,3,4,5,6])
print(e)  # int  float  string  
"""

# head tail info  describe :

a= pd.Series([10,20,30,40,50,60,70,80,90,100],index=[11,12,13,14,15,16,17,18,19,20])

# print(a)
# print(a.head())  # by default  5 rows print
# print(a.head(3))  # print  first  3 rows
# print(a.tail())   # by default  last 5 rows print
# print(a.tail(3))   #   last 3 rows print

# print(a.info())   #  info
# print(a.describe())   #  describe
# print(a.shape)

"""
c= pd.Series({"ram":90,"sita":97,"raj":91,"dhan":92,"bhagwat":94})
print(c)
print(c.keys())
print(c.values)
"""

# read_csv : 

# df =pd.read_csv("pandas_backup\student_tops.csv")
# print(df)
# print(df.shape)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe(include="all"))

# tsv : tab separated values
"""
df =pd.read_csv("pandas_backup\student_tops_copy.tsv",sep="\t")
print(df)
"""
# excel file  : 

import openpyxl   # pip install openpyxl

df= pd.read_excel("pandas_backup\sample-staff-data.xlsx")
print(df.head())
print(df.columns)
