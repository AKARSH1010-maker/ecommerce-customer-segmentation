import os
import pandas as pd

file_path = r"C:\Users\akars\OneDrive\Desktop\archive (2)\OnlineRetail.csv"

if not os.path.exists(file_path):
    print("File not found:", file_path)
else:
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        print("Shape:", df.shape)
        print("\nColumns:\n", df.columns.tolist())
        print("\nInfo:")
        print(df.info())
        print("\nFirst 5 rows:")
        print(df.head())
    except Exception as e:
        print("Error while loading file:", e)
        print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
# Remove missing values
df = df.dropna(subset=['CustomerID', 'Description'])

# Remove duplicates
df = df.drop_duplicates()

# Remove negative quantity
df = df[df['Quantity'] > 0]

# Remove negative price
df = df[df['UnitPrice'] > 0]

# Convert date column
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("\nAfter cleaning shape:", df.shape)
print("\nCleaned preview:\n", df.head())
# Save cleaned dataset
df.to_csv("outputs/cleaned_data.csv", index=False)

print("\nCleaned data saved to outputs/cleaned_data.csv")
# Basic KPIs
print("\nTotal Revenue:", df['TotalPrice'].sum())
print("Total Customers:", df['CustomerID'].nunique())
print("Total Products:", df['Description'].nunique())
print("Total Transactions:", df['InvoiceNo'].nunique())
# Top 10 selling products
top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Selling Products:\n")
print(top_products)
# Monthly sales trend
df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['TotalPrice'].sum().reset_index()

print("\nMonthly Sales Trend:\n")
print(monthly_sales.head())
# Top selling item per month
monthly_item_sales = df.groupby(['Month', 'Description'])['Quantity'].sum().reset_index()

top_items_per_month = monthly_item_sales.loc[
    monthly_item_sales.groupby('Month')['Quantity'].idxmax()
]

print("\nTop Selling Item Per Month:\n")
print(top_items_per_month.head())
# Top selling item per month
monthly_item_sales = df.groupby(['Month', 'Description'])['Quantity'].sum().reset_index()

top_items_per_month = monthly_item_sales.loc[
    monthly_item_sales.groupby('Month')['Quantity'].idxmax()
]

print("\nTop Selling Item Per Month:\n")
print(top_items_per_month.head(12))
# Create RFM table
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

print("\nRFM Table:\n")
print(rfm.head())
from sklearn.preprocessing import StandardScaler

rfm_features = rfm[['Recency', 'Frequency', 'Monetary']]

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_features)

print("\nRFM scaled shape:", rfm_scaled.shape)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

inertia = []
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)

print("\nInertia values:", inertia)

plt.figure(figsize=(8,5))
plt.plot(K, inertia, marker='o')
plt.title("Elbow Method For Optimal Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.show()
# Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

print("\nCluster counts:\n")
print(rfm['Cluster'].value_counts())

print("\nClustered RFM preview:\n")
print(rfm.head())
# Cluster summary
cluster_summary = rfm.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean()

print("\nCluster Summary:\n")
print(cluster_summary)
# Label clusters
def label_customer(row):
    if row['Cluster'] == 0:
        return 'Regular Customers'
    elif row['Cluster'] == 1:
        return 'High Value Customers'
    elif row['Cluster'] == 2:
        return 'At Risk Customers'
    else:
        return 'Low Value Customers'

rfm['Segment'] = rfm.apply(label_customer, axis=1)

print("\nCustomer Segments:\n")
print(rfm[['CustomerID','Cluster','Segment']].head())
# ==============================
# Cluster distribution
# ==============================
print("\nSegment Counts:\n")
print(rfm['Segment'].value_counts())


# ==============================
# Save customer segments
# ==============================
rfm.to_csv("outputs/customer_segments.csv", index=False)
print("\nCustomer segments saved to outputs/customer_segments.csv")


# ==============================
# Save monthly sales
# ==============================
monthly_sales.to_csv("outputs/monthly_sales.csv", index=False)


# ==============================
# Save top items per month
# ==============================
top_items_per_month.to_csv("outputs/top_items_per_month.csv", index=False)


# ==============================
# Visualization - Customer Segments
# ==============================
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.scatterplot(data=rfm, x='Frequency', y='Monetary', hue='Segment')
plt.title("Customer Segments (Frequency vs Monetary)")
plt.show()


# ==============================
# Visualization - Recency vs Monetary
# ==============================
plt.figure(figsize=(10,6))
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Segment')
plt.title("Customer Segments (Recency vs Monetary)")
plt.show()


# ==============================
# Visualization - Segment Count
# ==============================
plt.figure(figsize=(8,5))
sns.countplot(data=rfm, x='Segment')
plt.title("Customer Segment Distribution")
plt.xticks(rotation=20)
plt.show()


print("\nProject analytics completed successfully")