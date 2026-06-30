import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# bar charts : 

"""df = pd.DataFrame({
    "student":["ram","sita","raj","dhan","bhagwat"],
    "marks":[90,55,85,65,75]
})

print(df)
x= np.arange(len(df["student"]))  # np.arange(10)  # start  end  step  np.arange(5)   # 01234

plt.figure(figsize=(10,5))
bars =plt.bar(df["student"],df["marks"],color="skyblue",width=0.5)
plt.title("student marks")
plt.xlabel("student")
plt.ylabel("marks")

for i in bars:  # bars = [ram ,sita ,ravan ,laxman ,dhan]
    plt.text(
        i.get_x() + i.get_width()/2,  # get_x() ===> coordinate x
        i.get_height()+1,
        i.get_height(),
        ha="center",   # horizontal alignment
        fontsize=10,
        color="black"
    )

plt.legend(labels=["marks"],loc='upper right')
plt.grid(True)
plt.show()
"""
# barh charts :
"""
df = pd.DataFrame({
    "sectors" :["Government","Education","Health","Industry","Agriculture"],
    "population":[100,200,150,400,900]
})
bars =plt.barh(df["sectors"],df["population"],color="skyblue",height=0.5)
width = 0.8
plt.title("population")
plt.xlabel("population")
plt.ylabel("sectors")
for i in bars:  # bars = [ram ,sita ,ravan ,laxman ,dhan]
    plt.text(
        i.get_width(),   # x 
        i.get_y() + i.get_height()/2,  # y
        # i.get_height()+1,
        # i.get_height(),
        i.get_width(),  # text
        ha="left",   # horizontal alignment
        va="center",   # vertical alignment
        fontsize=10,
        color="black",
        style="italic"
    )
plt.grid(True)
plt.show()
"""
# plt.ylim(0,100)   # change the y axis range.  

# pie charts : percent divide  

"""
mobile =["iphone","android","windows","samsung","htc"]
shares = [78,56,34,61,20]

plt.pie(shares,labels=mobile,autopct="%1.1f%%")
plt.title("mobile share")
plt.show()
"""

# donut charts :
mobile =["iphone","android","windows","samsung","htc"]
shares = [78,56,34,61,20]

plt.pie(shares,labels=mobile,autopct="%1.1f%%",wedgeprops={'width':0.6})
plt.title("mobile share")
plt.show()


# next : overlapping function  , wraptext function  
# task  : 1 using  flipkart data set : bar chart ,  barh , pie , donut 