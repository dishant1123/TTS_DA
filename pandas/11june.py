# column ,loc,iloc ,multiple col, query ,condition : 

import pandas as pd 

df =pd.read_csv("pandas\mckinsey.csv")
# print(df)

# print  specific rows : 

"""
one_col =df['country']
print(one_col)
"""
# multiple row  print : 

"""
mul_col =df[['country',"year",'population']]
print(mul_col)
"""

# loc : label  based 

# a=df.loc[0]
# a=df.loc[1]
a=df.loc[2:5]  # 2 index start  5 index   ===> note  : last  value included .
# a=df.loc[2:5,["country","population"]]    # 2:5 row  ,col : name 
print(a)