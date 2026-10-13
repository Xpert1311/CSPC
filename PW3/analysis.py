import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, mannwhitneyu, pearsonr



# SESSION 1

print("--- SESSION 1: Data Shape & Head ---")
df_heart = pd.read_csv("heart.csv")
print("Shape:", df_heart.shape)
print(df_heart.head())

cols = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()
for i, col in enumerate(cols):
    axes[i].hist(df_heart[col], bins=20, edgecolor='black', alpha=0.7)
    axes[i].set_title(col)
plt.tight_layout()
plt.savefig("distributions.png")
print("\nSaved distributions.png")

print("\n--- Normality Tests ---")
for col in cols:
    stat, p = shapiro(df_heart[col])
    print(f"{col}: p-value = {p:.4g} (Normal? {'Yes' if p > 0.05 else 'No'})")



# SESSION 2

print("\n--- SESSION 2: Heart Disease vs Max Heart Rate (thalach) ---")
healthy = df_heart[df_heart['target'] == 0]['thalach']
disease = df_heart[df_heart['target'] == 1]['thalach']

stat, p_mw = mannwhitneyu(disease, healthy)
print(f"Mann-Whitney U p-value: {p_mw:.4g}")
print(f"Healthy Mean: {healthy.mean():.2f} ± {healthy.sem():.2f}")
print(f"Disease Mean: {disease.mean():.2f} ± {disease.sem():.2f}")

plt.figure(figsize=(6, 5))
plt.bar(['Healthy (0)', 'Disease (1)'], [healthy.mean(), disease.mean()], 
        yerr=[healthy.sem(), disease.sem()], capsize=10, color=['green', 'red'], alpha=0.7)
plt.ylabel('Mean Max Heart Rate (thalach)')
plt.title('Max Heart Rate by Disease Status')
plt.savefig("thalach_groups.png")
print("Saved thalach_groups.png")

corr, p_corr = pearsonr(df_heart['age'], df_heart['thalach'])
print(f"\nAge vs Thalach Correlation: {corr:.4f} (p={p_corr:.4g})")
plt.figure(figsize=(6, 5))
plt.scatter(df_heart['age'], df_heart['thalach'], alpha=0.5, edgecolor='k')
m, b = np.polyfit(df_heart['age'], df_heart['thalach'], 1)
plt.plot(df_heart['age'], m*df_heart['age'] + b, color='red')
plt.xlabel("Age")
plt.ylabel("Thalach")
plt.title(f"Age vs Max Heart Rate (r = {corr:.2f})")
plt.savefig("age_thalach.png")
print("Saved age_thalach.png")

print("\n--- Chemical Mystery ---")
df_chem = pd.read_csv("chemicals_cancer.csv")
corr_b, _ = pearsonr(df_chem['benzene'], df_chem['malignancy'])
corr_c, _ = pearsonr(df_chem['cadmium'], df_chem['malignancy'])
print(f"Naive Benzene-Malignancy: {corr_b:.4f}")
print(f"Naive Cadmium-Malignancy: {corr_c:.4f}")

subset = df_chem[(df_chem['pollution_index'] > 45) & (df_chem['pollution_index'] < 55)]
corr_b_sub, _ = pearsonr(subset['benzene'], subset['malignancy'])
corr_c_sub, _ = pearsonr(subset['cadmium'], subset['malignancy'])
print("\nAfter controlling for pollution (index 45-55):")
print(f"Subset Benzene-Malignancy: {corr_b_sub:.4f}")
print(f"Subset Cadmium-Malignancy: {corr_c_sub:.4f}")

print("\n--- Bonus ---")
print(df_heart['target'].value_counts(normalize=True))