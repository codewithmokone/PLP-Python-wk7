import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1
# Loading the dataset
df = pd.read_csv('sales.csv') 

# Using head() to display 5 records
display_head = df.head(10)
print("Displaying 10 records: ", display_head)

# Checking data types and missing values
types_values = df.info()
print("Data types and missing values: ", types_values) 

# Dropping missing value
drop_values = df.dropna()
print(drop_values.to_string())

# Task 2
# Question 1
basic_stats = df.describe()
print("Basic Stats: \n", basic_stats)

#Question 2
group_means = df.groupby('Discount').mean()
print('Group by: \n', group_means)


#Task 3
# Set a style for plots
sns.set_theme(style='whitegrid')

#1. Line Chart – Trend Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(data=display_head, x='Sales_Rep', y='Sales_Amount', marker='o')  # Replace columns
plt.title('Sales Per Month')
plt.xlabel('Sales Rep')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar Chart – Comparison
plt.figure(figsize=(8, 5))
category_means = display_head.groupby('Region')['Sales_Amount'].mean().sort_values()
sns.barplot(x=category_means.index, y=category_means.values)
plt.title('Sales Per Region')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Histogram
plt.figure(figsize=(8, 5))
sns.histplot(display_head['Discount'], kde=True, bins=20, color='skyblue')  # Replace with your column
plt.title('Discounts Applied')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

### 4. Scatter Plot – Relationship Between Two Numeric Columns ###
plt.figure(figsize=(8, 5))
sns.scatterplot(data=display_head, x='Sales_Amount', y='Discount')
plt.title('Relationship Between Sales and Discount')
plt.xlabel('Sales')
plt.ylabel('Discount')
plt.tight_layout()
plt.show()