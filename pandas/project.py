import pandas as pd
import openpyxl   # pip install openpyxl
# df = pd.read_excel("pandas\Online Retail.xlsx")

# print(df.isnull().sum())
# df = df.dropna(subset=["CustomerID", "Description"])
# print(df)
# print(df.info())

"""
1. insights  : 
total  revenue  
total order  : df['invoice'].value_count()
total customer :df['cutomer_id'].value_count()

total  product : 

top_10 selling  product  :df.groupby(desc)[qty].sum()sort_value(asc =false) .head(10)

highest revenue  of product:  df.groupby(desc)[revenue].sum()sort_value(asc =false) .head(10)


top_10 selling  customer  

contry wise  sales 
orders by country  

avg order value 
monthly revenue 
daily , hrs  

avg product  price 

higest_qty_purchase  : groupby()
most_exp product groupby()

pivort for :country vs month ,country vs product 

=============================================================
1. Top Revenue Country : using idxmax ===> idxmax() returns the index label of the maximum value in a Series or DataFrame column. 

2. Best Selling Product
3. Highest Revenue Product
4. Best Customer
5. Peak Sales Month
6. Peak Sales Hour
7. Average Order Value
8. Top 10 Customers
9. Countries with Low Revenue
10. Products with Low Sales


"""
# ==========================================
# Step 1: Import Libraries
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering


# ==========================================
# Step 2: Create Dataset
# ==========================================

data = {
    "Student": ["A", "B", "C", "D", "E", "F"],
    "Maths": [20, 22, 80, 82, 25, 78],
    "Science": [25, 24, 81, 84, 28, 79]
}

df = pd.DataFrame(data)

print("="*50)
print("Original Dataset")
print("="*50)
print(df)


# ==========================================
# Step 3: Select Features
# ==========================================

X = df[["Maths", "Science"]]

print("\nSelected Features")
print(X)


# ==========================================
# Step 4: Create Linkage Matrix
# ==========================================

linked = linkage(X, method="ward")

print("\nLinkage Matrix")
print(linked)


# ==========================================
# Step 5: Draw Dendrogram
# ==========================================

plt.figure(figsize=(8,5))

dendrogram(
    linked,
    labels=df["Student"].values
)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Students")
plt.ylabel("Distance")

plt.show()


# ==========================================
# Step 6: Apply Agglomerative Clustering
# ==========================================

model = AgglomerativeClustering(
    n_clusters=2,
    linkage="ward"
)

clusters = model.fit_predict(X)

df["Cluster"] = clusters


# ==========================================
# Step 7: Display Result
# ==========================================

print("\nFinal Cluster Result")
print(df)


# ==========================================
# Step 8: Plot Clusters
# ==========================================

plt.figure(figsize=(7,6))

plt.scatter(
    df["Maths"],
    df["Science"],
    c=df["Cluster"],
    s=150
)

# Student Labels
for i in range(len(df)):
    plt.text(
        df["Maths"][i]+0.5,
        df["Science"][i]+0.5,
        df["Student"][i],
        fontsize=12
    )

plt.title("Hierarchical Clustering")
plt.xlabel("Maths Marks")
plt.ylabel("Science Marks")
plt.grid(True)

plt.show()


# ==========================================
# Step 9: Print Students in Each Cluster
# ==========================================

print("\nStudents in Each Cluster")

for cluster in sorted(df["Cluster"].unique()):
    print(f"\nCluster {cluster}")
    print(df[df["Cluster"] == cluster][["Student", "Maths", "Science"]])