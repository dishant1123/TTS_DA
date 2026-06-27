"""
pip install matplotlib
pip install seaborn
Introduction to Visualization : 

python  : graphs :  2 lib  
1. matplotlib :
        a.plot  ===> line plot
        b. scatter  ===> scatter plot
        c. bar  ===> bar plot
        d. hist  ===> histogram
        e. boxplot  ===> box plot
        f. pie  ===> pie plot
    
    ===> statistical function  , simple  graphs     
2. seaborn :
    a.barplot  ===> bar plot
    b.scatterplot  ===> scatter plot
    c.heatmap 

    ===> attractive  graphs  , complex  graphs , relationship between  two  variables
    
ex : matplot lib properties : 
   x axis , y axis ,title ,size,color ,xlabel ,ylabel ,show    
    
"""
# ex :1 line plot  

from matplotlib import pyplot as plt 
import pandas as pd

sales = pd.DataFrame({
    'month' :[1,2,3,4,5,6,7,8,9,10,11,12],
    'sales' :[100,200,150,400,350,600,720,680,900,1000,1150,1190]
})

# print(sales)  # linewidth = thickness,linestyle = line style , marker = shape of marker

plt.plot(sales['month'],sales['sales'],color='red',linewidth=2,linestyle='-',marker='o')
plt.title("monthly sales")
plt.xlabel("month")
plt.ylabel("sales")
plt.grid(True)
plt.legend(labels=['sales'],loc='upper left')
plt.show()

# analysis how to trend going  ?? 


