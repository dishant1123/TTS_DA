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

# drop_duplicates ,IQR ,Z-score ,apply:

import pandas as pd 

df =pd.DataFrame({
    "id" :[101,102,103,104,105,106,107,108], 
    "product":["monitor","keyboard","mouse","monitor","keyboard","mouse","CPU","keyboard"],
    "price":[50000,1200,800,30000,1000,500,15000,150000],
    "quantity":[10,5,2,8,1,3,4,6]
})

print(df)
# df = df.drop_duplicates(subset=["product"])
# print(df)

# IQR : outlier   formula  : IQR = Q3 - Q1

"""
q1 = df["price"].quantile(0.25)
q3 = df["price"].quantile(0.75)
print(q1,q3)
IQR = q3 - q1
print("IQR :",IQR)

# lower bound  : Q1 - 1.5 * IQR
# upper bound  : Q3 + 1.5 * IQR

lower_bound = q1 - 1.5 * IQR
upper_bound = q3 + 1.5 * IQR
print("lower bound :",lower_bound)  # -50
print("upper bound :",upper_bound)  # 86

# print outlier : 

outlier = df[(df['price']>upper_bound) | (df['price']<lower_bound)]
print(outlier)
"""

# apply   : 
"""df["Revenue"] = df["price"] * df["quantity"]
print(df)
"""
# apply  : 

df['category'] =df.apply(lambda x :  "a" if x['price'] >10000 else "b" , axis=1)
print(df)


"""
lambda x :"a" if x > 100 else "b"
"""
