"""
1. query  : condition  
2. sort_value , sort_index,reset_index ,reindex 
3. dropna , fillna 
4. isnull , isnull.sum()
"""

import pandas as pd
"""
df = pd.read_csv("pandas\mckinsey.csv")
print(df)
"""
# task  : 1 country  =="india" and year ==2002 print country  and year column using  loc or  iloc  or df . 

"""
result = df.loc[(df["country"] =="India") & (df["year"] ==2002)]
print(result)
"""
# task  : 2 country  =="Iceland" and life_exp >75  print country  and life_exp column using  loc or  iloc  or df . 

"""result = df.loc[(df["country"] =="Iceland") & (df["life_exp"] >75),["country","life_exp"]]
print(result)
"""

# df.query : using  for  condition  ,  filter  and also  multiple  condition . 
"""
df=pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name" :["ram","sita","raj","dhan","bhagwat"] ,
    "age" :[12,34,56,45,34] ,
    "salary" :[1200,3400,5600,4500,3400]
})
# print(df)

# print salary  > 10000 
result = df.query("salary >5000")
print(result)

# multiple  condition : age >15 and salary >3000 
result = df.query("salary >3000 & age >15")
result = df.query("salary >3000 | age >10")
print(result)

"""

# sort_value , sort_index,reset_index ,reindex : 

"""
df=pd.DataFrame({
    "id" :[10,24,3,40,5],
    "name" :["ram","sita","raj","dhan","bhagwat"] ,
    "age" :[12,34,56,45,34] ,
    "salary" :[12000,3400,56000,45000,3200]
})
"""
# print(df)

# sort_salary_wise = df.sort_values(by="salary")  # by default  ===> asc to desc 
# print(sort_salary_wise)

# sort ===> desc to  asc : 
"""
sort_salary_wise = df.sort_values(by="salary",ascending=False)
print(sort_salary_wise)
"""
# task :4 using csv using  sort_value function  display top 5 population . desc to asc  
# task  : 5 country  =="Iceland" and life_exp >75  print country  and life_exp column using  query function . 

# sort_index : 

# sort_index_wise = df.sort_index(ascending=False)
# print(sort_index_wise)

# reset_index : 
"""reset_index_wise = sort_index_wise.reset_index(drop=True)
print(reset_index_wise)
"""

# isnull , isnull.sum()
import numpy as np 

df=pd.DataFrame({
    "id" :[10,24,np.nan,40,5],
    "name" :["ram","sita",np.nan,"dhan","bhagwat"] ,
    "age" :[12,34,56,45,34] ,
    "salary" :[np.nan,3400,np.nan,45000,3200]
})

print(df)
# print(df.isnull())  # bool   ===> missing  value  ===> TRUE
# print(df.isnull().sum())   # missing  count  ===> col-wise 

# dropna : 
# df.dropna(inplace=True)
# df.dropna(axis=0,inplace=True)  # row wise  ===> delete 
# df.dropna(axis=1,inplace=True)   # col wise ===> delete 
# print(df)

# fillna : 

# df= df.fillna(0)  # null  value  replace with 0 
# print(df)

# salary none then  put mean or avg : 
# df['salary']=df['salary'].fillna(df['salary'].mean())
df['salary']=df['salary'].fillna(100)

print(df)

df.index =["A","B","C","D","E"]
print(df)