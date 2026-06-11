# pandas : pip install  pandas 

# use : 
"""
1. data cleaning
2. data manupulation
3. data analysis
4. sort ,merge (join), filter
5. any  file read ===> csv ,tsv ,excel ,sqlfile,txt 

why  important ds / DA ? 

"""
"""
1. seris   : 1d data structure 
2. dataframe : 2d data structure  
"""
import  pandas as pd 
import  numpy as np 

"""a= pd.Series([1,2,3,4,5])
print(a)

b= pd.Series([23,45,67,89],index=["a","b","c","d"])
print(b)

c= pd.Series({"ram" :90,"sita":78,"ravan":67})  # d1 ={12:78}
print(c)
"""
# dataframe : 2d data structure  
"""
table  : 

srno    name    age  marks  
1       ram     12    98
2       sita    34    87
3       raj     56    78    row  * col 
"""

# dataframe  : 2 ways 
"""
1. 1 ways  : dict 
2. 2 ways  : list of list
"""
"""
df =pd.DataFrame({
    "id" :[1,2,3,4,5], 
    "name" :["ram","sita","raj","dhan","bhagwat"] ,
    "age" :[12,34,56,45,34] ,
    "salary" :[1200,3400,5600,4500,3400] 
})
print(df)
print(df.columns)

"""
"""df1 =pd.DataFrame([
    [1,"ram",23,90000],
    [2,"sita",34,89999],
    [3,"ravan",45,67000]  
],columns=["id","name","age","salary"])
print(df1)
print(df1.shape)
"""

# info , describe , descibe (include =all) ,head  , tail  : 

# df =pd.DataFrame({
#     "id" :[1,2,np.nan,4,5], 
#     "name" :["ram","sita","raj","dhan","bhagwat"] ,
#     "age" :[12,34,56,45,34] ,
#     "salary" :[1200,3400,5600,4500,3400] 
# })

# print(df)
# print(df.head())   # default 5 rows 
# print(df.head(2))   # first 2   rows 
# print(df.tail())   # default 5 rows
# print(df.tail(3))   # last 3 rows

# print(df.info())
# print(df.describe())
# print(df.describe(include="all"))

# read_csv () :

# df = pd.read_csv("pandas\student_tops.csv")
df = pd.read_csv("pandas\student.tsv",sep="\t")
print(df)