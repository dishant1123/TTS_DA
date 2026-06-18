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
"""
df["Revenue"] = df["price"] * df["quantity"]
print(df)
"""
# apply  : 


"""df['category'] =df.apply(lambda x :  "a" if x['price'] >10000 else "b" , axis=1)
print(df)
"""

# lambda : one  line  liner  function  
"""
a=int(input("enter a number :"))
b=int(input("enter a number :"))

if a>b :
    print("a")
else :
    print("b")

syntax :  lambda arg : expression     

result = lambda a,b : print(a) if (a>b) else print(b)
result(12,45)
"""
"""
lambda x :"a" if x > 100 else "b"
"""
"""def func(price):
    if price >10000 :
        return "10%"
    else :
        return "5%"
    
df["discount"] = df['price'].apply(func)
print(df)
"""
# map : i want  to  rs symbol  to all num value  :₹ 
"""df["Revenue"] = df["price"] * df["quantity"]

df_num = df[['price','Revenue']]
update_df = df_num.map(lambda x : f"₹{x}")

print(update_df)

"""

# l1 =[12,23,56,78]   # +5  = [17 ,28 ,61 , 83]
# # result =list(map(lambda x : x+5 ,l1))
# result =tuple(filter(lambda x : x>50 ,l1))

# print(result)


"""df["Revenue"] = df["price"] * df["quantity"]
print(df)

df_num = df[['price','Revenue']]
update_df = df_num.map(lambda x : f"${x}")

print(update_df)
"""
"""
input  : ram 
output  : how are you ram  ???  hey ram  how are  you  ??
"""
# a=input("enter a string :")
# print("how are you ??",a)
# print("hey",a,"how are you ??")
# print(f"hey {a}  how are  you ")


from scipy .stats import zscore

df['z-score'] =zscore(df['price'])
print(df)
outliers = df[df["z-score"] > 2]
print(outliers)
