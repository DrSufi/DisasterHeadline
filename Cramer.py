import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load your dataset
df = pd.read_excel("DisasterNews1May2025.xlsx")

# Clean the 'Country' field if necessary
df['Country'] = df['Country'].str.strip()

# Assume a 'Topic' column already exists; otherwise, assign mock topics for testing
# (Replace this with your actual topic modeling results)
# Example: df['Topic'] = your_precomputed_topics
import random
random.seed(42)
df['Topic'] = random.choices(['Topic 1', 'Topic 2', 'Topic 3', 'Topic 4', 'Topic 5'], k=len(df))

# Function to compute Cramér’s V
def cramers_v(confusion_matrix):
    chi2, _, _, _ = chi2_contingency(confusion_matrix)
    n = confusion_matrix.to_numpy().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    return np.sqrt(phi2 / min(k - 1, r - 1))

# 1. Disaster Type vs Topic
contingency_disaster = pd.crosstab(df['Disaster Type'], df['Topic'])
cramers_v_disaster = cramers_v(contingency_disaster)

# 2. Country vs Topic
contingency_country = pd.crosstab(df['Country'], df['Topic'])
cramers_v_country = cramers_v(contingency_country)

# Print results
print("Cramér’s V for Disaster Type vs. Topic:", round(cramers_v_disaster, 3))
print("Cramér’s V for Country vs. Topic:", round(cramers_v_country, 3))
