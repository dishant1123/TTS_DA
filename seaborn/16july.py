"""
1. distribution  plot  :sales_trans_csv ,amt,bins =20 
2. KDE plot  : show the  density ,kernel density estimation 
3. Hist +kde : sales_trans_csv ,amt,bins =20,kde=true 
4. box plot  : x =amount  , category  wise ====> x=category ,y=amt
5. violin plot : combination of the box +kde ===> it shown the spread and density of the data.
6. box + violin :sns.violinplot category  wise ====> x=category ,y=amt ,inner=box

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("seaborn\sales_transactions_dataset.csv")
print(df.head())

"""
sns.histplot(x="Amount",data=df,bins=20)
plt.title("distribution plot")
plt.show()
"""
# kde plot :  show the  density ,kernel density estimation , on basis  of probability density function

"""sns.kdeplot(x="Amount",data=df,fill=True)
plt.title("KDE plot")
plt.show()
"""
# kde + hist plot : 
"""sns.histplot(x="Amount",data=df,bins=20,kde=True)
plt.title("distribution plot")
plt.show()
"""

# box  plot  : 

"""
sns.boxplot(x='Amount',data=df)
plt.title("box plot")
plt.show()
"""
# category wise box plot :

"""sns.boxplot(x="Category",y="Amount",data=df,hue="Category")
plt.title("box plot category wise")
plt.show()
"""

# violin plot : combination of the box +kde ===> it shown the spread and density of the data.

"""sns.violinplot(
    x="Category",
    y="Amount",
    data=df,
    hue="Category",
    inner="box",
    cut=0,
    scale="count",
    palette="Set1"
)
plt.title("violin plot")
plt.show()
"""
