"""
create  dataframe  : 
    id , name , age , salary
    
1. head () , tail ()
2. find  missing value  in age and salary  and  print  count  of  missing value and then fill  with mean value
3. convert name  in to upper case 
4. if salary >50000 then  person  included in  A category  else  B category

"""

# datetime  : 
import  pandas as pd

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


df["joining_date"] = pd.to_datetime(df["joining_date"])

df['year'] = df['joining_date'].dt.year
df['month'] = df['joining_date'].dt.month
df['day'] = df['joining_date'].dt.day
df["months_name"] =df['joining_date'].dt.month_name()

df['today'] =pd.Timestamp.today().strftime("%Y-%m-%d")
df["total_days"] =df['today'] -df['joining_date']  # hw : 
print(df)
"""
"""
id   joining_date   year  month  day
101  2020-01-01     2020  1      1
                     joining_date     today()      today()- joining_date
                     "2020-01-10",    2026-06-20
                     "2020-02-01",    2026-06-20
                     "2020-03-21",    2026-06-20
                     "2020-04-30",    2026-06-20
                     "2020-05-31",    2026-06-20
                     "2020-06-13",    2026-06-20
                     "2020-07-29",    2026-06-20
                     "2020-08-31"     2026-06-20

"""
"""
import datetime 
from datetime import datetime
import math 
today =datetime.today().strftime("%d-%m-%Y")
print(today)

print(math.pow(2,3))
"""   # 23 /4 /2020  ===> 23-04-2020

# join  : 
"""
1. inner join : at least one  value  must  match
2. left join : at least one  value  must  match  and  add  left 
3. right join : at least one  value  must  match  and  add  right
4. outer join  : combine  row  and  column  unmatch value 
"""

# pd.merge () : 

customers = pd.DataFrame({
    "id" :[101,102,103,104,105],
    "name":["ram","sita","raj","dhan","bhagwat"],
    "city" :["mumbai","delhi","bangalore","hyderabad","chennai"]
})

products = pd.DataFrame({
    "id" : [1022,1023,1024,1205,1206],
    "product":["monitor","keyboard","mouse","CPU","printer"],
    "price":[50000,1200,800,30000,10000]
})

"""inner_join = pd.merge(
    customers,
    products,
    on ="id",
    how ="inner"
)
print(inner_join)
"""
"""right_join = pd.merge(
    customers,
    products,
    on ="id",
    how ="right"
)
print(right_join)

"""
"""
left_join = pd.merge(
    customers,
    products,
    on ="id",
    how ="left"
)
print(left_join)
"""

outer_join = pd.merge(
    customers,
    products,
    on ="id",
    how ="outer"
)
print(outer_join)

# concat  :