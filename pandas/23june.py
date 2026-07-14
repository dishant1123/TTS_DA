# task  : movie and director  join  

import pandas as pd

"""movies = pd.read_csv("pandas\movies.csv")
directors = pd.read_csv("pandas\directors.csv")

movies =movies.drop(columns ="Unnamed: 0")
directors =directors.drop(columns ="Unnamed: 0")

print(movies)
print(directors)

movie_directors= pd.merge(
    movies,
    directors,
    left_on="director_id",
    right_on="id",
    how="left"
)
print(movie_directors.head())
"""

# concate : 
"""
jan_sales = pd.DataFrame({
    "product_id":[101,102,103,104,105],
    "product_name":["monitor","keyboard","mouse","CPU","printer"],
    "sales":[100,200,300,400,500]
})

feb_sales = pd.DataFrame({
    "product_id":[106,107,108,109,110],
    "product_name":["monitor","keyboard","mouse","CPU","printer"],
    "sales":[10000,20000,30000,40000,50000]
})

jan_feb_sales = pd.concat([jan_sales,feb_sales])
print(jan_feb_sales)
print(pd.concat([jan_sales,feb_sales]))
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

# sales_purchase = pd.concat([sales,purchases],axis=1)  # col wise  concate
sales_purchase = pd.concat([sales,purchases],axis=0)  # row wise concate 
print(sales_purchase)
"""

# pivot : 
import pandas as pd


sales_data = pd.DataFrame({
    "Date": [
        "2026-01-01", "2026-01-01", "2026-01-02",
        "2026-01-02", "2026-01-03", "2026-01-03",
        "2026-01-04", "2026-01-04"
    ],
    "Region": [
        "North", "South", "North", "South",
        "East", "West", "East", "West"
    ],
    "Product": [
        "Laptop", "Laptop", "Mouse", "Mouse",
        "Keyboard", "Keyboard", "Laptop", "Mouse"
    ],
    "Sales": [
        50000, 45000, 5000, 6000,
        8000, 7000, 55000, 6500
    ]
})

print(sales_data)

#  product  wise  sales ===> sum 
"""pivort = sales_data.pivot_table(
    columns="Product",
    values="Sales",
    aggfunc="sum"
    
)
print(pivort)
"""
# region  wise  sales ===> sum 
pivort = sales_data.pivot_table(
    columns="Region",
    values="Sales",
    aggfunc="sum"
    
)
print(pivort)


# groupby :

employees = pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['John','Jane','Bob','Alice','David'],
    'department':['HR','Sales','Sales','HR','Finance'],
    'salary':[5000,6000,4500,7000,5500]
})

print(employees)

department_wise_salary =employees.groupby('department')['salary'].sum()
print(department_wise_salary)


# next session : pd.get_dummies()