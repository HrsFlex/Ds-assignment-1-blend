import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style='whitegrid')

# Load data
file_path = '2.13.Practical-example.Descriptive-statistics-exercise-solution.xlsx'
print("Loading data...")
df = pd.read_excel(file_path, sheet_name='365RE', header=4)
print("Data loaded. Shape:", df.shape)

# Task 1: Variable Types (Printed in Notebook, skipping here or just printing)
print("\n--- Task 1: Variable Types ---")
print("See notebook for full table.")

# Task 2: Histogram (267 bins)
print("\n--- Task 2: Histogram (267 bins) ---")
plt.figure(figsize=(12, 6))
plt.hist(df['Price'], bins=267, color='skyblue', edgecolor='black')
plt.title('Histogram of Price (267 bins)')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('task2_histogram.png')
print("Saved task2_histogram.png")

# Task 3: Histogram (100k bins)
print("\n--- Task 3: Histogram (100k bins) ---")
min_price = df['Price'].min()
max_price = df['Price'].max()
bins = np.arange(min_price, max_price + 100000, 100000)

plt.figure(figsize=(12, 6))
plt.hist(df['Price'], bins=bins, color='salmon', edgecolor='black')
plt.title('Histogram of Price (Bin width $100,000)')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.xticks(bins, rotation=45)
plt.savefig('task3_histogram.png')
print("Saved task3_histogram.png")

# Task 5: Scatter Plot
print("\n--- Task 5: Scatter Plot ---")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Area (ft.)', y='Price', data=df, alpha=0.6)
plt.title('Scatter Plot: Price vs Area')
plt.xlabel('Area (ft.)')
plt.ylabel('Price')
plt.savefig('task5_scatterplot.png')
print("Saved task5_scatterplot.png")

# Task 6: Frequency Table
print("\n--- Task 6: Frequency Table ---")
country_counts = df['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Frequency']
country_counts['Relative Frequency'] = country_counts['Frequency'] / country_counts['Frequency'].sum()
country_counts['Cumulative Frequency'] = country_counts['Relative Frequency'].cumsum()
print(country_counts)

# Task 7: Pareto Diagram
print("\n--- Task 7: Pareto Diagram ---")
fig, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(x='Country', y='Frequency', data=country_counts, ax=ax1, color='steelblue')
ax1.set_ylabel('Frequency')
ax1.set_xlabel('Country')
ax2 = ax1.twinx()
sns.lineplot(x='Country', y='Cumulative Frequency', data=country_counts, ax=ax2, color='red', marker='o', sort=False)
ax2.set_ylabel('Cumulative Frequency')
ax2.set_ylim(0, 1.1)
plt.title('Pareto Diagram: Country')
plt.savefig('task7_pareto.png')
print("Saved task7_pareto.png")

# Task 8: Descriptive Stats
print("\n--- Task 8: Descriptive Stats ---")
price_stats = {
    'Mean': df['Price'].mean(),
    'Median': df['Price'].median(),
    'Mode': df['Price'].mode()[0],
    'Skewness': df['Price'].skew(),
    'Variance': df['Price'].var(),
    'Standard Deviation': df['Price'].std()
}
for stat, value in price_stats.items():
    print(f"{stat}: {value:.2f}")

# Task 10: Covariance and Correlation
print("\n--- Task 10: Covariance and Correlation ---")
covariance = df['Price'].cov(df['Area (ft.)'])
correlation = df['Price'].corr(df['Area (ft.)'])
print(f"Covariance: {covariance:.2f}")
print(f"Correlation: {correlation:.4f}")
