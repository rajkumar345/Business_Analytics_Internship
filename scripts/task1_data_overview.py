# Task 1: Data Overview

import pandas as pd

# 1. Load dataset
df = pd.read_csv(r"../data/Data_set 2.csv")   # adjust path if needed

# 2. Overview
print("Shape (rows, columns):", df.shape)
print("\nColumn Info:")
print(df.info())

# 3. Preview
print("\nSample Rows:")
print(df.head())

# 4. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

# 6. Descriptive stats
print("\nDescriptive Statistics:")
print(df.describe(include="all"))

# Save cleaned dataset if you do cleaning later
# df.to_csv("../outputs/cleaned_dataset.csv", index=False)