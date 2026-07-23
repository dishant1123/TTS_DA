# regression  plot  , adv style   in seaborn:

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"""
df=pd.read_csv("seaborn/sales_discount.csv")
print(df.head())
"""
# plt.figure(figsize=(10,5))

"""sns.regplot(
    data=df,
    x="Discount",
    y="Sales",
    ci=None,  # confidence intervals,
    scatter_kws={"s": 100}
)
plt.title("Sales vs Discount")
plt.show()

"""

# lmplot :
"""
sns.lmplot(
    data=df,
    x="Discount",
    y="Sales",
    col="Region",
    height=4

)
plt.show()
"""

# adv style :1. sns.set_theme() sns.set_palette(),sns.set_context()

# sns.set_theme(
# sns.set_theme(style="darkgrid")
# sns.set_theme(style="whitegrid")
"""sns.set_theme(style="ticks")



sns.regplot(
    data=df,
    x="Discount",
    y="Sales",
    ci=None,  # confidence intervals,
)
plt.show()

"""

# color palette :

"""# sns.set_theme(style="ticks")
# sns.set_palette("deep")
# sns.set_palette("pastel", n_colors=5)
sns.set_palette("colorblind")


sns.regplot(
    data=df,
    x="Discount",
    y="Sales"
    # ci=None  # confidence intervals,
)
plt.show()

"""

# sns.set_context : 

"""
# sns.set_context("paper")
# sns.set_context("talk")
# sns.set_context("poster")
sns.set_context("notebook")

sns.regplot(
    data=df,
    x="Discount",
    y="Sales"
    # ci=None  # confidence intervals,
)
plt.show()
"""

# corporate style :

"""sns.set_theme(
    style="whitegrid",
    palette="deep",
    context="talk"
)

plt.figure(figsize=(10,5))

sns.regplot(
    data=df,
    x="Discount",
    y="Sales",
    scatter_kws={"s": 100},
    line_kws={"linewidth": 3}
)
plt.title("Sales vs Discount")
plt.xlabel("Discount")
plt.ylabel("Sales")
plt.show()
"""