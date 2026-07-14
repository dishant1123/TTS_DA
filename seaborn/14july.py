"""
matplotlib : basic graph  

    1. line  plot  : trend line  
    2. bar plot    : comparison
    3. scatter plot: relationship 
    4. pie chart   : percentage,perportion
    5. donut chart : percentage,perportion
    6. box  plot   : outlier 
    7. hist  plot  : frequency 

function  : 
    figsize,xlabel,ylabel,title,legend,grid,show,linewidth,linestyle,marker,color,savefig 
    
seaborn : adv graph , statistical calculation  ,less code 

pip install seaborn ,!pip install seaborn 

seaborn theme  : sns.set_theme(darkgrid,whitegrid,white,ticks)

1. lineplot : id vs purchase 
2.
axes level : 
| Function          |
| ----------------- |
| sns.lineplot()    |
| sns.scatterplot() |
| sns.barplot()     |
| sns.countplot()   |
| sns.boxplot()     |
| sns.violinplot()  |
| sns.histplot()    |
| sns.kdeplot()     |
| sns.heatmap()     |
| sns.regplot()     |



figure level  : 

| Function         |
| ---------------- |
| sns.relplot()    |
| sns.catplot()    |
| sns.displot()    |
| sns.jointplot()  |
| sns.pairplot()   |
| sns.lmplot()     |
| sns.clustermap() |


1. count plot : gender ,city  ===> use hue =gender 
2. bar        : gen vs  pur ,city vs  pur amt : using  estimator  : sum , np.median ,min,max,error bar=none   


"""
# ex :1 mat using  line  plot 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy  as np

"""
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=[10,20,30,40,50,60,70,80,90,100,110,120]
plt.style.use('ggplot')

plt.plot(x,y)
plt.title("line plot")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid(True)
plt.show()
"""

# ex :2 csv file 

df = pd.read_csv("seaborn\customer_data.csv")
print(df.head())

sns.set_theme(style="darkgrid")
plt.figure(figsize=(10,6))
"""
lines =sns.lineplot(x="Customer_ID",y="Purchase_Amount",data=df,hue="Gender",linewidth=2,markers=True)

for i in lines.lines:
    i.set_linewidth(2)
    i.set_marker('o')
    i.set_markersize(10)
    i.set_markeredgewidth(2)

plt.title("line plot")

plt.title("line plot")
plt.show()
"""
# ex :2 count plot  

# sns.countplot(x="Gender",data=df)
"""
sns.countplot(x="City",data=df)

plt.title("count plot")
plt.show()
"""

# ex : 3 bar plot 

"""sns.barplot(x="Gender",y="Purchase_Amount",data=df,estimator=max,errorbar=None,hue="City")
plt.title("bar plot")
plt.show()
"""

df1 =sns.load_dataset("tips")
print(df1.head())
print(df1.tail())