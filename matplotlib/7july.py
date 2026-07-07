"""
1. plt.style.use()   ggplot, bmh, classic, Solarize_Light2 ===> plot  for mon vs sales, month vs target .

2. adv charts : using  monthly_performance.csv
    a.stacked bar chart  : bar  ===> mon vs col , mon vs gro 
    b.area plot  : plt.stackplot
    c.errorbar plot : using student_marks .csv 
    d.time seris chart  : using time_series.csv

"""

import pandas as pd
import matplotlib.pyplot as plt

"""df = pd.read_csv("matplotlib\sales_data.csv")

plt.style.use("bmh")
plt.figure(figsize=(10,6))

plt.plot(df['Month'],df['Sales'],color='blue',marker='o',linestyle='-',linewidth=2)
plt.xlabel("month")
plt.ylabel("sales")

plt.plot(df['Month'],df['Target'],color='red',marker='o',linestyle='-',linewidth=2)
plt.title("monthwise target  and sales")
plt.xlabel("month")
plt.ylabel("target")
plt.grid(True)
plt.legend(["sales","target"],loc='upper left')
plt.show()
"""

# advance  charts :

#1. stacked bar chart  : bar  ===> mon vs col , mon vs gro

"""
df = pd.read_csv("matplotlib\monthly_performance.csv")

plt.style.use("classic")
plt.figure(figsize=(10,6))

plt.bar(df['Month'],df['Electronics'],color='blue',width=0.5)
plt.bar(df['Month'],df['Clothing'],color='red',width=0.5)
plt.bar(df['Month'],df['Grocery'],color='green',width=0.5)


plt.title("monthly performance")
plt.xlabel("month")
plt.ylabel("performance")
plt.legend(["electronics","clothing","grocery"],loc='upper left')
plt.grid(True)
plt.show()
"""

# b.area plot  : plt.stackplot
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("matplotlib\monthly_performance.csv")

# df.style.use("Solarize_Light2")

"""plt.stackplot(df['Month'],df['Electronics'],df['Clothing'],df['Grocery'],labels=["electronics","clothing","grocery"])

plt.title("monthly performance")
plt.xlabel("month")
plt.ylabel("performance")
plt.legend(["electronics","clothing","grocery"],loc='upper left')
plt.grid(True)
plt.show()
"""

# time seris chart  : using time_series.csv

"""df = pd.read_csv("matplotlib/time_series.csv")

df['Date'] =pd.to_datetime(df['Date'])

plt.plot(df['Date'],df['Revenue'],color='blue',marker='o',linestyle='-',linewidth=2)
plt.title("revenue vs date")
plt.xlabel("date")
plt.ylabel("revenue")
plt.show()
"""

#c.errorbar plot : using student_marks .csv


df =pd.read_csv("matplotlib\student_marks.csv")

plt.figure(figsize=(10,6))

plt.errorbar(df['Student'],df['Average'],yerr=df['StdDev'],color='blue',marker='o',linestyle='-',linewidth=2)
plt.title("student marks")
plt.xlabel("student")
plt.ylabel("marks")
plt.show()