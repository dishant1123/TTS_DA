import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# bar charts : 

df = pd.DataFrame({
    "student":["ram","sita","raj","dhan","bhagwat"],
    "marks":[90,55,85,65,75]
})

print(df)
x= np.arange(len(df["student"]))  # np.arange(10)  # start  end  step  np.arange(5)   # 01234

plt.figure(figsize=(10,5))
plt.bar(df["student"],df["marks"],color="skyblue",width=0.5)
plt.title("student marks")
plt.xlabel("student")
plt.ylabel("marks")

"""
for i in range(len(x)):
    plt.text(
        i.get_x() + i.get_width()/2,
        i.get_height()+1,
        i.get_height(),
        ha="center",   # horizontal alignment
        fontsize=12,
        color="red"
    )
"""
plt.legend(labels=["marks"],loc='upper right')
plt.grid(True)
plt.show()

# label in bar chart  :

