# ================================
# STEP 1: Import Libraries
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Style for better plots
sns.set(style="darkgrid")

# ================================
# STEP 2: Load Dataset
# ================================

india_unemp_data = pd.read_csv("Unemployment in India.csv")

# ================================
# STEP 3: Data Cleaning
# ================================

# Rename columns (IMPORTANT for uniqueness)
india_unemp_data.columns = ["States", "Date", "Frequency", "Unemployment_Rate",
              "Estimated_Employed", "Estimated_Labour_Participation", "Region"]

# Convert Date column
india_unemp_data["Date"] = pd.to_datetime(india_unemp_data["Date"], dayfirst=True)

# Drop missing values
india_unemp_data = india_unemp_data.dropna()

# ================================
# STEP 4: Basic Analysis
# ================================

print("Dataset Info:\n")
print(india_unemp_data.info())

print("\nStatistical Summary:\n")
print(india_unemp_data.describe())
# ================================
# CUSTOM INSIGHT (ADD HERE)
# ================================

highest_state = india_unemp_data.groupby("States")["Unemployment_Rate"].mean().idxmax()
print("State with highest unemployment:", highest_state)

# ================================
# STEP 5: Unemployment by Region
# ================================

region_data = india_unemp_data.groupby("Region")["Unemployment_Rate"].mean().sort_values()

plt.figure(figsize=(10,5))
sns.barplot(x=region_data.index, y=region_data.values)
plt.xticks(rotation=45)
plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate")
plt.show()

# ================================
# STEP 6: State-wise Analysis
# ================================

state_data = india_unemp_data.groupby("States")["Unemployment_Rate"].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(x=state_data.index, y=state_data.values)
plt.xticks(rotation=90)
plt.title("State-wise Unemployment Rate")
plt.xlabel("States")
plt.ylabel("Unemployment Rate")
plt.show()

# ================================
# STEP 7: Time Series Analysis
# ================================

time_data = india_unemp_data.groupby("Date")["Unemployment_Rate"].mean()

plt.figure(figsize=(12,5))
plt.plot(time_data.index, time_data.values)
plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Rate")
plt.show()

# ================================
# STEP 8: Correlation Heatmap
# ================================

plt.figure(figsize=(8,5))
# Take only numeric columns
numeric_data = india_unemp_data.select_dtypes(include=['number'])
sns.heatmap(numeric_data.corr(), annot=True)
plt.show()
plt.title("Correlation Heatmap")
plt.show()
# ================================
# EXTRA GRAPH (ADD HERE)
# ================================

plt.figure(figsize=(8,5))
sns.histplot(india_unemp_data["Unemployment_Rate"], bins=20, kde=True)
plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate")
plt.ylabel("Frequency")
plt.show()