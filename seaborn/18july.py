"""
Pairplot (Multivariate Analysis) Topics: Pairplot for numerical features Hue parameter Scatter + KDE diagonals Demo: Pairplot for case study numeric variables

Jointplot Topics: Types: scatter, hexbin, KDE Relationship analysis Demo: Sales vs Profit jointplot
"""

# pair plot :

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("seaborn\sales_data (1).csv")
print(df)

sns.pairplot(
    data=df,
    vars=['Sales','Profit','Quantity','Discount'],
    hue="Region",
    kind="scatter"
             )
plt.title("pair plot")
plt.show()


# jointplot :
