import pandas as pd


"""df = pd.DataFrame({
    "id" :[101,102,103,104,105,106,107,108],
    "joining_date" :["2020-01-10",
                     "2020-02-01",
                     "2020-03-21",
                     "2020-04-30",
                     "2020-05-31",
                     "2020-06-13",
                     "2020-07-29",
                     "2020-08-31"]
})

print(df)

df['joining_date'] = pd.to_datetime(df["joining_date"])
# print(df.info())
df['year'] =df['joining_date'].dt.year
df['month'] =df['joining_date'].dt.month
df['month'] =df['joining_date'].dt.month_name()
df['day'] =df['joining_date'].dt.day

print(df)
"""
# hw  : total_days stay  emp in  our company .hint  : import datetime  ==>today()

# join :
"""
1. inner join  : at least one  value  must  match
2. left join   : at least one vaue must match and add left 
3. right join  : at least one vaue must match and add right 
4. outer join  : unmatch value combine
"""

# pd.merge () :

customers = pd.DataFrame({
    "id":[101,102,103,104,105],
    "name":["ram","sita","raj","dhan","bhagwat"],
    "city":["mumbai","delhi","bangalore","hyderabad","chennai"]
})
products = pd.DataFrame({
    "id":[101,102,103,104,105],
    "product":["monitor","keyboard","mouse","CPU","printer"],
    "price" :[50000,1200,800,30000,10000]
})

"""inner_join  = pd.merge(
    customers,
    products,
    on="id",
    how="right"
)
print(inner_join)
"""  

"""left_join = pd.merge(
    customers,
    products,
    on="id",
    how="left"
)
print(left_join)
"""
"""right_join = pd.merge(
    customers,
    products,
    on="id",
    how="left"
)
print(right_join)
"""

# hw : join  movies.csv and  directors.csv ===> using director_id vs  id 

# concate :

"""feb_sales = pd.DataFrame({
    "product_id":[101,102,103,104,105],
    "product_name" :["monitor","keyboard","mouse","CPU","printer"],
    "sales" :[10000,20000,30000,40000,50000]
})

dec_sales = pd.DataFrame({
    "product_id":[106,107,108,109,110],
    "product_name" :["monitor","keyboard","mouse","CPU","printer"],
    "sales" :[100,200,300,400,500]
})

feb_dec_sales = pd.concat([feb_sales,dec_sales])
print(feb_dec_sales)
"""
# col wise  concate  :

"""sales = pd.DataFrame({
    "user_id" :[101,102,103,104,105],
     "sales" :[100,200,300,400,500]   
})

purchases = pd.DataFrame({
    "id" :[106,107,108,109,110],
    "purchases" :[10000,20000,30000,40000,50000]
})

sales_pur = pd.concat([sales,purchases],axis=1)  # col wise  concate
print(sales_pur)

sales_pur = pd.concat([sales,purchases],axis=0)  # row wise  concate
print(sales_pur)
"""
"""
1.calculate the sales   = price *qty 
2.univarite analysis : age distribution  ,product frequency  : using value_count (),city frequency ,avg rating 
3.histogram  :age , boxplot :price
4. bivariate analysis :analysis of  two variable 
	a. sales vs age  :scatter 
	b. qty vs sales :scatter 
	c. product wise avg sales 
	d. Gender-wise Average Sales
	e. City-wise Sales
	f. Product vs Quantity
5. stats :sales mean , median ,mode , std ,var 
6. correlation  : corr(number)
	Close to 1 → Strong positive relationship
	Close to -1 → Strong negative relationship
	Close to 0 → No linear relationship
"""

import pandas as pd
import matplotlib.pyplot as plt    # pip install pyplot.matplotlib
import seaborn as sns

sales_data = pd.DataFrame({
    "Customer_ID":[101,102,103,104,105,106,107,108,109,110],
    "Age":[22,25,28,40,30,45,26,38,50,33],
    "Gender":["Male","Female","Female","Male","Female","Male","Male","Female","Male","Female"],
    "City":["Ahmedabad","Surat","Rajkot","Ahmedabad","Vadodara",
            "Surat","Rajkot","Ahmedabad","Vadodara","Surat"],
    "Product":["Laptop","Mobile","Laptop","Tablet","Mobile",
               "Laptop","Tablet","Mobile","Laptop","Tablet"],
    "Quantity":[1,2,1,3,2,1,4,2,1,3],
    "Price":[65000,25000,70000,30000,22000,68000,28000,24000,72000,32000],
    "Rating":[4.8,4.2,4.6,4.0,3.8,4.9,4.1,4.3,4.7,4.2]
})

df = pd.DataFrame(sales_data)
df["total_sales"]=df["Quantity"] * df["Price"]
print(df)

# univarite analysis : 

age_distribution = df["Age"].value_counts()
product_frequecy = df['Product'].value_counts()
city_frequecy = df['City'].value_counts()
rating_frequecy = df['Rating'].value_counts()

# print(age_distribution)
# print(product_frequecy)
print(city_frequecy)
print(rating_frequecy)

# age  histogram : 

"""hist_age = df['Age'].hist(bins=7)
plt.show()
"""

# box plot  : 

"""plt.boxplot(df['Price'])
plt.xlabel("Price")
plt.title("Boxplot of Price")
plt.show()
"""

# bivariate analysis :
	# a. sales vs age  :scatter 

"""
sns.scatterplot(x="Age",y="total_sales",data=df)
plt.xlabel("Age")
plt.ylabel("Total Sales")
plt.title("Scatterplot of Total Sales vs Age")
plt.show()
"""
# sales vs qty : 
"""sns.scatterplot(x="Quantity",y="total_sales",data=df)
plt.xlabel("QTY")
plt.ylabel("Total Sales")
plt.title("Scatterplot of Total Sales vs QTY")
plt.show()
"""
# product  wise avg sales  : 

"""
Product_wise_sales =df.groupby('Product')['total_sales'].mean()
print(Product_wise_sales)

# City-wise Sales
city_wise_sales =df.groupby('City')['total_sales'].sum()
print(city_wise_sales)
"""

# stats : mean , median ,mode , std ,var

"""df['total_sales'] =df['total_sales'].mean()
print(df['total_sales'])

df['total_sales'] =df['total_sales'].median()
print(df['total_sales'])

df['total_sales'] =df['total_sales'].var()
print(df['total_sales'])

df['total_sales'] =df['total_sales'].std()
print(df['total_sales'])
"""

# co-relation  : 

graph = df.corr(numeric_only=True)

sns.heatmap(graph,annot=True,cmap="coolwarm")
plt.show()