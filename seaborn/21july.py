"""

SESSION 8 - Relational Plots (Scatter, Line, Regressions) Topics: sns.relplot() sns.scatterplot() sns.lineplot() Demo: Category-wise month-wise trend line

1. joint plot  :
2. heatmap :
3. 
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

"""
df=pd.read_csv("seaborn\sales_heatmap_dataset.csv")
print(df)

coorelation =df.corr(numeric_only=True)
sns.heatmap(coorelation,annot=True,cmap="YlGnBu")

plt.title("sales heatmap")
plt.show()
"""

#scatter plot :
df =pd.read_csv("seaborn\category_monthly_sales.csv")
print(df)
plt.figure(figsize=(10,6))
"""# sns.scatterplot(data=df,x="Quantity",y="Revenue")
sns.scatterplot(data=df,x="Quantity",y="Revenue",hue="Category")

plt.title("scatter plot")
plt.show()
"""

# line plot  : 
"""sns.lineplot(data=df,x="Quantity",y="Revenue",markers=True,hue="Category",errorbar=None)
plt.title("line plot")
plt.show()
"""

#relplot :

"""sns.relplot(data=df,x="Quantity",y="Revenue",hue="Category",kind="scatter")
plt.title("line plot")
plt.show()
"""
# regplot :

sns.regplot(data=df,x="Quantity",y="Revenue",line_kws={"color":"red","linestyle":"-","linewidth":2})
plt.title("reg plot")
plt.show()

# hw :using flipkart data set  make  the graph for heatmap() , corr , scatterplot(),regplot()
