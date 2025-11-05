# Task 2: Gender Distribution

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load cleaned data (or raw if no cleaning done)
df = pd.read_csv("../data/Data_set 2.csv")

# 2. Standardize gender
df['gender'] = df['gender'].astype(str).str.strip().str.title()

mapping = {
    'M': 'Male', 'Male': 'Male', 'male': 'Male',
    'F': 'Female', 'Female': 'Female', 'female': 'Female',
    'Other': 'Other', 'O': 'Other', 'Non-Binary': 'Other', 'Na': 'Unknown'
}
df['Gender_clean'] = df['gender'].map(mapping).fillna('Unknown')

# 3. Counts
counts = df['Gender_clean'].value_counts()
percentages = df['Gender_clean'].value_counts(normalize=True) * 100

print("\nGender Counts:\n", counts)
print("\nGender Percentages:\n", percentages.round(2))

# 4. Visualization - Bar Chart
plt.figure(figsize=(6,4))
counts.plot(kind='bar', color='skyblue')
plt.title('Gender Distribution - Counts')
plt.xlabel('gender')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("../outputs/gender_bar_chart.png")
plt.show()

# 5. Visualization - Pie Chart
plt.figure(figsize=(6,6))
counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution - Percentage')
plt.ylabel('')
plt.tight_layout()
plt.savefig("../outputs/gender_pie_chart.png")
plt.show()