# pandas : pip install pandas 
"""
use : 
1.data cleaning 
2.data manupulation
3.data analysis
4. sorting  , merge  , join 

why pandas is important for data analysis : 

1. Seris :  
2. DataFrame :  
"""
import  pandas as pd
import numpy as np 
# seris : 1 dementional  data structure . 

"""
a = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(a)

b= pd.Series([12,34,56,78.89,"hello",True],index=[1,2,3,4,5,6])
print(b)

c= pd.Series([12,34,56,78,90],index=["ram","sita","raj","dhan","bhagwat"])
print(c)

d= pd.Series({"ram":12,"sita":34,"raj":56,"dhan":78,"bhagwat":90})
print(d)
"""

# head tail info  describe : 

"""
a = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(a)

print(a.head())  # by default  5 rows print 
print(a.head(3))  # print  first  3 rows   
print(a.tail())   # by default  last 5 rows print   
print(a.tail(3))   #   last 3 rows print   
print(a.info())   #  info
print(a.describe())   #  describe
print(a.shape)
"""

# dataframe : 2 dementational  data structure .

"""
ex : 
srno     name     age     marks  
1        ram      12       98
2        sita     34       87
3        raj      56       78
4        dhyan    78       90

"""
# create dataframe  manually : 
"""
2 ways  : 
1.  create dataframe  from dict
2.  create dataframe  from list of list
"""
"""
df = pd.DataFrame({
    "id" : [1,2,3,4,5] , 
    "name" : ["ram","sita","raj","dhan","bhagwat"] ,
    "age" : [12,34,56,45,34] ,
    "salary" :[1200,3400,5600,4500,3400] 
}) 

print(df)
print(df.shape)
"""
"""
df1 =pd.DataFrame([
    [1,"ram",34,90000],
    [2,"sita",56,80000],
    [3,"raj",78,70000],
    [4,"dhan",78,90000],
    [5,"bhagwat",90,np.nan]
],columns=["id","name","age","salary"])

print(df1)
"""

# dataframe : head tail info  describe : 

"""
df = pd.DataFrame({
    "id" : [1,2,3,4,5] , 
    "name" : ["ram","sita","raj","dhan","bhagwat"] ,
    "age" : [12,34,56,45,34] ,
    "salary" :[1200,3400,5600,4500,3400]
}) 

print(df)
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.describe(include="all"))
"""

# read csv file  : 

"""
df = pd.read_csv("pandas\mckinsey.csv")
print(df)
print(df.columns)

df1=pd.read_csv("pandas\student.tsv",sep="\t")
print(df1)

df2 =pd.read_json("pandas\student2.json")
print(df2)
"""

df = pd.read_csv("pandas\studebt3.csv")
print(df)

# export  : 

