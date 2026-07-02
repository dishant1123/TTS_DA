# using flipcart dataset : 

import pandas as pd
import  matplotlib.pyplot as plt


df =pd.read_csv("pandas//flipkart_orders.csv")

print(df)

# check missing values : 

# print(df.isnull().sum())

# drop  ==> cutomer top 10 customer  
# age  ===> fillna().mean()
#  city ,state ,rating ===> drop 
# review ===> fillna() ===> print avg 

# line  , bar , pie , donut  ,barh  :monthwise  sales  

# analysis : line graph  ===> month wise sales 

order_date = pd.to_datetime(df['order_date'])
# total_sales = df['revenue']
# print(order_date.head())
# print(total_sales.head())

df['month_wise'] =pd.to_datetime(df['order_date']).dt.month_name()

group_wise = df.groupby('month_wise')['revenue'].sum()
print(group_wise)


line_plot = plt.plot(group_wise.index,group_wise.values,color='blue',marker='o',linestyle='-',linewidth=2)
plt.title("Monthwise Sales")
plt.ylim(500000,3500000)
width =0.5
for x,y in zip(group_wise.index,group_wise.values):
    plt.text(
        x,  # 
        y,  # 
        y,  # text  
        ha='center',
        va='bottom',
        fontsize=9,
        color='blue',
    )
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# year  wise sales trend :  2022 ,23 ,24 