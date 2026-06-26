import pandas as pd
import openpyxl   # pip install openpyxl
df = pd.read_excel("pandas\Online Retail.xlsx")

# print(df.isnull().sum())
# df = df.dropna(subset=["CustomerID", "Description"])
# print(df)
print(df.info())

"""
1. insights  : 
total  revenue  
total order  : df['invoice'].value_count()
total customer :df['cutomer_id'].value_count()

total  product : 

top_10 selling  product  :df.groupby(desc)[qty].sum()sort_value(asc =false) .head(10)

highest revenue  of product:  df.groupby(desc)[revenue].sum()sort_value(asc =false) .head(10)


top_10 selling  customer  

contry wise  sales 
orders by country  

avg order value 
monthly revenue 
daily , hrs  

avg product  price 

higest_qty_purchase  : groupby()
most_exp product groupby()

pivort for :country vs month ,country vs product 

=============================================================
1. Top Revenue Country : using idxmax ===> idxmax() returns the index label of the maximum value in a Series or DataFrame column. 

2. Best Selling Product
3. Highest Revenue Product
4. Best Customer
5. Peak Sales Month
6. Peak Sales Hour
7. Average Order Value
8. Top 10 Customers
9. Countries with Low Revenue
10. Products with Low Sales


"""
