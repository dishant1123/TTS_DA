"""
1. query
2.sort_value , sort_index,reset_index ,reindex
3. dropna , fillna
4.isnull, isnull.sum()
"""
import pandas as pd
import  numpy as np

# df = pd.read_csv("pandas\mckinsey.csv")

# task :1  country  =="india" and year ==2002 print country  and year column using  loc or  iloc  or df .

"""
result = df.loc[(df['country']=="India") & (df['year']==2002),['country','year']]
print(result)
"""
# task  :2 country  =="Iceland" and life_exp >75  print country  and life_exp column using  loc or  iloc  or df .
"""
result = df.loc[(df['country']=="Iceland") | (df['life_exp']>75),['country','life_exp','year']]
print(result)
"""

# query  :

"""
df= pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name" :["ram","sita","raj","dhan","bhagwat"],
    "age" :[12,34,56,45,34],
    "salary" :[12000,3400,56000,4500,32000]
})
"""

# print salary > 4000 

"""
result = df.query("salary > 4000")[['name','salary']]
print(result)
"""
# print salary > 4000 and age > 15

"""result = df.query("salary > 4000 & age >15")[['name','age','salary']]
print(result)
"""

#sort_value , sort_index,reset_index ,reindex :

"""sort_salary_wise = df.sort_values(by="salary")  # by default   ===> asc to desc
# sort_salary_wise = df.sort_values(by="salary",ascending=False)  # by default   ===> asc to desc

print(sort_salary_wise)   
"""

# task :4 using csv using  sort_value function  display top 5 population .

# sort_index : 

"""sort_index_wise = df.sort_index(ascending=False)
print(sort_index_wise)
"""
# reset_index : 
"""reset_index_wise =sort_index_wise.reset_index(drop=True)
print(reset_index_wise) 
"""

# dropna . fillna : 

df= pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name" :["ram",np.nan,"raj","dhan","bhagwat"],
    "age" :[12,34,56,45,np.nan],
    "salary" :[np.nan,3400,56000,np.nan,32000]
})

print(df)   # np.nan ===> whole dataset convert  into   ===> float  

# print(df.isnull())  # give  true  ===> missing  value  ===> TRUE
# print(df.isnull().sum())   # missing  count  ===> col-wise

# print(df.dropna(axis=0))  # row wise   ===> by default  row wise 
# print(df.dropna(axis=1))  # col wise  


# fillna  : 

# df =df.fillna(0)
# print(df)

# age ===> missing value ===>    fill with mean  . 

# df['age'] =df['age'] .fillna(df['age'].mean()).astype(int)
df['salary'] =df['salary'] .fillna(df['salary'].mean()).astype(int)
print(df)

