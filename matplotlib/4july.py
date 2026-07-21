"""
1. scatter plot  : advertisement vs sales  ===> use this data frame 
2. scatter  plot with trend line :
3. show equation  :

4. subplot : 
df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":[120,150,170,160,200,220],
    "Profit":[20,30,35,28,45,50],
    "Expenses":[100,120,135,132,155,170],
    "Customers":[250,270,300,290,340,380]
})

5.df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"],
    "Sales":[120,135,150,170,180,200,220,240]
})

style  : ["ggplot",
          "bmh",
          "classic",
          "Solarize_Light2"] 

"""
# ex :1 scatter plot : 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.DataFrame({
    "advertisement":[10,20,30,40,50,60],
    "sales":[120,150,175,200,250,230]
})

plt.figure(figsize=(10,5))
plt.scatter(df['advertisement'],df['sales'],color='blue',marker='o',s=100)
plt.title("scatter plot")
plt.xlabel("advertisement")
plt.ylabel("sales")
plt.show()

# trend line :

"""plt.figure(figsize=(10,5))
plt.scatter(df['advertisement'],df['sales'],color='blue',marker='o',s=100)

m,b =np.polyfit(df['advertisement'],df['sales'],1)

plt.plot(df['advertisement'],m*df['advertisement']+b,color='red',linestyle='-',linewidth=2)
plt.title("scatter plot with trend line")
plt.xlabel("advertisement")
plt.ylabel("sales")
plt.show()
"""

# sub plot  : 
"""df = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":[120,150,170,160,200,220],
    "Profit":[20,30,35,28,45,50],
    "Expenses":[100,120,135,132,155,170],
    "Customers":[250,270,300,290,340,380]
})

print(df)

plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.plot(df['Month'],df['Sales'],color='blue',marker='o',linestyle='-',linewidth=2)
plt.title("monthwise sales")

plt.subplot(2,2,2)
plt.bar(df['Month'],df['Profit'],color='red',width=0.5)
plt.title("monthwise profit")

plt.subplot(2,2,3)
plt.scatter(df['Customers'],df['Expenses'],color='green',marker='o',s=100)
plt.title("customers vs expenses")

plt.subplot(2,2,4)
plt.plot(df['Sales'],df['Profit'],color='black',marker='o',linestyle='-',linewidth=2)
plt.title("sales vs profit")

plt.tight_layout()  # automatically adjust subplot layout
plt.show()
"""

