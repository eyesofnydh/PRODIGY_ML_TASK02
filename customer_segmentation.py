import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Correct file path to the customer data CSV file
data = "Mall_Customers.csv"

# Load data into a pandas DataFrame
try:
    df = pd.read_csv(data)  # Use pd.read_csv() to read the data from the CSV file
except FileNotFoundError:
    print(f"File not found. Please ensure the file '{data}' is in the correct directory.")
    exit()

# Select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# Add the cluster labels to the DataFrame
df['Cluster'] = kmeans.labels_

# Plotting the clusters
plt.figure(figsize=(10, 8))
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=df['Cluster'], cmap='viridis', marker='o', s=100, alpha=0.6, edgecolors='w')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segments')
plt.colorbar(label='Cluster')
plt.grid(True)
plt.show()

# Print the first few rows of the dataframe to verify cluster assignments
print(df.head())
