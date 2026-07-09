# annoations :
# PPT : 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("matplotlib\month_wise_sale.csv")

plt.figure(figsize=(10,6))

plt.plot(df['Month'],df['Sales'],color='blue',marker='o',linestyle='-',linewidth=2)
plt.title("monthwise sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid(True)

# find  out the  max sale , and  max sales index : 

max_sale = df['Sales'].max()  # 380 
max_sale_index =df['Sales'].idxmax()  # 11 

higest_sale_month = df.loc[max_sale_index,'Month']  # 'Nov'

# print(max_sale)
# print(max_sale_index)
# print(higest_sale_month)

plt.scatter(max_sale_index,max_sale,color='red',marker='o',s=100)
# plt.show()

plt.annotate("max sales",(max_sale_index,max_sale),color='red',fontsize=10)
plt.show()
