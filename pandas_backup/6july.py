"""
task :1 

create dataframe id , name ,age ,salary   ===> 8 rows 
1.head () , tail ()
2. salary ==> null , age  ===> null  ==> count missing  count null value 
3. missing  value  fill  ===> salary ,age missing value  ===> mean 
4. top 3 salary  with name  
5. bottom 3 salary  with name  with age 
6. drop id  column 

"""

# outlier :
import pandas as pd

df =pd.DataFrame({
    "id" :[101,102,103,104,105,106,107,108], 
    "product":["monitor","keyboard","mouse","monitor","keyboard","mouse","CPU","keyboard"],
    "price":[50000,1200,800,30000,1000,500,15000,150000],
    "quantity":[10,5,2,8,1,3,4,6]
})
print(df)

# IQR :  inter quartile range

"""
IQR = Q3 - Q1 
  
"""
"""q1 =df['price'].quantile(0.25)
q3 =df['price'].quantile(0.75)
print(q1,q3)    # q1 = 950  , q3 =35000 

IQR = q3 - q1
print("IQR :",IQR)  # IQR : 34050.0

lower_bound= q1 -1.5 *IQR    # 950 - 1.5*34050
upper_bound= q3 +1.5 *IQR    # 35000 + 1.5* 34050 

print("lower bound :",lower_bound)  # lower bound :-50
print("upper bound :",upper_bound)  # upper bound : 86 

outlier =df[(df['price'] > upper_bound) | (df['price'] < lower_bound)]
print(outlier)
"""

# z score : 

from scipy.stats import zscore
"""
df['z-score'] = zscore(df['price'])
print(df)
outlier = df[df["z-score"] > 2]
print(outlier)
"""

#apply  : 

"""def func(price):
    if price >10000 :
        return "10%"
    else :
        return "5%"

df['discount']=df['price'].apply(func)
print(df) 
"""
# price ,revenue : rs symbol  to all num value  :₹

df['revenue'] = df['price'] * df['quantity']
print(df)     # price = ₹10000 , quantity = 10 , revenue = ₹100000

df_num = df[['price','revenue']]   # 50000 ,150000
rs_symbol = df_num.map(lambda x : f"₹{x}")

print(rs_symbol)

l1=[2,5,7,9,12]   # each element  * 5   
"""l2=[]
for i in l1 : 
    l2.append(i*5)
print(l2)"""

# r=list(map(lambda x : x * 5,l1))  # it given  new  list  
# r=list(filter(lambda x : x > 5,l1))  # filter  the  list print  values > 5 
# print(r)

