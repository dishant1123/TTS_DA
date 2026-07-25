import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 

df =pd.read_csv("seaborn/bank-full.csv",sep=";")
# print(df)
# print(df.head())

# basic info : shape ,info ,describe,isnull.sum()
"""print(df.shape)
print(df.info())
print(df.describe())
print(df.describe(include="all"))
print(df.isnull().sum())
print(df.duplicated().sum())
"""

# target variable :
print(df['y'].value_counts())  # most customer said no , very few subscriber  

# age  distribution :

"""plt.figure(figsize=(10,5))

sns.histplot(df["age"],bins=30,kde=True)
plt.title("Age Distribution")
plt.show()
# conclusion :  majority of customer  age is  younger or older ??? ====> 30-45 years old
"""
# subscription by age :
"""
plt.figure(figsize=(10,5))
sns.boxplot(
    data=df,
    x='y',
    y='age'
)
plt.show()

# conclusion : are older customers more likely to subscribe ? no 
"""

# job wise analysis :

"""plt.figure(figsize=(10,5))
sns.countplot(
    data=df,
    y='job',
    order=df['job'].value_counts().index
)

plt.show()
"""
#conculsion : which job is  highest customer ?   blue collar ,management  

#job vs subscription :

"""pd.crosstab(df['job'],df['y'])
sns.countplot(
    data=df,
    y='job',
    hue='y',
)

plt.show()
# which  category is subscribe more  ??   # management 
"""

# marital status :
# education  
