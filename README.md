# PRODIGY_ML_TASK02


Customer Segmentation using K-means Clustering

This repository contains a Python script that applies the K-means clustering algorithm to segment customers of a retail store based on their purchase history. The clustering is performed on the features "Annual Income (k$)" and "Spending Score (1-100)".

Dataset
The dataset Mall_Customers.csv includes the following columns:

CustomerID: Unique identifier for each customer
Gender: Gender of the customer
Age: Age of the customer
Annual Income (k$): Annual income of the customer in thousands of dollars
Spending Score (1-100): A score assigned by the retail store based on customer behavior and spending nature
Project Structure
customer_segmentation.py: Main script to load data, apply K-means clustering, and visualize the clusters.
Mall_Customers.csv: Dataset containing customer information.

Requirements
To run this project, you need the following Python packages:

pandas
matplotlib
scikit-learn

You can install the required packages using pip:
pip install pandas matplotlib scikit-learn

cd customer-segmentation
Ensure you have the dataset file Mall_Customers.csv in the same directory as the script.

Run the script:
python customer_segmentation.py

The script will:
Load the customer data into a pandas DataFrame from Mall_Customers.csv.
Select the relevant features ("Annual Income (k$)" and "Spending Score (1-100)").
Apply K-means clustering to segment the customers.
Visualize the resulting clusters using a scatter plot.
Print the first few rows of the DataFrame with the cluster assignments.

Example Output
The script will display a scatter plot showing the customer segments based on their annual income and spending score. Each segment will be represented by a different color.

 ![image](https://github.com/eyesofnydh/PRODIGY_ML_TASK02/blob/main/Figure_1.png)
 
   CustomerID  Gender  Age  Annual Income (k$)  Spending Score (1-100)  Cluster
0           1    Male   19                  15                      39        4
1           2    Male   21                  15                      81        3
2           3  Female   20                  16                       6        4
3           4  Female   23                  16                      77        3
4           5  Female   31                  17                      40        4


Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.
