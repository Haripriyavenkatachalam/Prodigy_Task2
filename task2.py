# -*- coding: utf-8 -*-
"""Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZGcmgpFBwu-fDan_dklIQmJwfVrJcFIn
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'shopping_trends_updated.csv'
df = pd.read_csv('/content/sample_data/shopping_trends_updated.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Data Cleaning: Handling missing values
# For example, replace missing values in 'Age' with the mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Data Cleaning: Remove duplicates
df.drop_duplicates(inplace=True)
# Data Exploration: Visualize the distribution of 'Age'
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=False, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in the Dataset')

# Data Exploration: Explore the relationship between 'Item Purchased' and 'Purchase Amount' using a box plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Item Purchased', y='Purchase Amount (USD)', data=df, palette='viridis')
plt.xlabel('Item Purchased')
plt.ylabel('Purchase Amount (USD)')
plt.title('Relationship between Item Purchased and Purchase Amount')

# Data Exploration: Correlation heatmap for numerical columns
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')

# Show the plots
plt.show()