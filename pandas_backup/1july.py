import pandas as pd 
# dataframe : 
"""
2 ways : 

1.dict  
2.list 
"""
# dict : 
"""
df =pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name" :["ram","sita","raj","dhan","bhagwat"],
    "age" :[20,30,40,50,60],
    "gender" :["male","female","male","female","male"]
})

print(df)
print(df.shape)
print(df.columns)
print(df.values)
"""
# list  : 

"""df=pd.DataFrame([
    [1,"ram",20,"male"],
    [2,"sita",30,"female"],
    [3,"raj",40,"male"],
    [4,"dhan",50,"female"],
],columns=["id","name","age","gender"])
print(df)
"""

# head tail info describe   describe_all  :

"""df =pd.DataFrame({
    "id" :[1,2,3,4,5],
    "name" :["ram","sita","raj","dhan","bhagwat"],
    "age" :[20,30,40,50,60],
    "gender" :["male","female","male","female","male"]
})
print(df.head(3))
print(df.tail(3))
print(df.info())
print(df.describe())
print(df.describe(include="all"))
"""

# loc  iloc :

df = pd.read_csv("pandas\mckinsey.csv")
# print(df)
# print(df.shape)

# loc  : 

print(df.loc[0])
print(df.loc[2:5])  # last value included
print(df.loc[1 :8 :2])  # start 1  stop 8   step 2 

print(df.loc[2:5,["country","population"]])  # last value included