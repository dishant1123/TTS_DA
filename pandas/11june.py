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

"""a=df.loc[0]
a=df.loc[1]
a=df.loc[2:5]  # 2 index start  5 index   ===> note  : last  value included .
a=df.loc[2:5,["country","population"]]    # 2:5 row  ,col : name 
a=df.loc[2:5,"continent":"gdp_cap"]    # 2:5 row  ,col : name 

print(a)
"""

# iloc : position based

# a=df.iloc[0]
# a=df.iloc[2:5]  # iloc  : last  excluded  
# a=df.iloc[2:10 :2]  # iloc  : last  excluded  2 step  
# a=df.iloc[2:5 , 1:3]    # 2:5 row  , 1:3 col   
# print(a)

"""
task  : 1 country  =="india" and year ==2002 print country  and year column using  loc or  iloc  or df . 
hint  : use & operator  for  condition 

task :2 in  mckinsey.csv dataset add new column col_name = next_year +3 display like  this  : 

    country,year,population,continent,life_exp,gdp_cap,next_year
0    Afghanistan,1952,8425333,Asia,28.801,779.4453145, 1955  
1    Afghanistan,1957,9240934,Asia,30.332,820.8530296, 1960
2    Afghanistan,1962,10267083,Asia,31.997,853.10071, 1965
3    Afghanistan,1967,11537966,Asia,34.02,836.1971382, 1970
4    Afghanistan,1972,13079460,Asia,36.088,739.9811058, 1975


"""
