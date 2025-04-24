import pandas as pd

df = pd.read_csv("results/merged.csv")
print("\nDescriptive Stats:\n")
print(df.describe())

print("\nNull Counts:\n")
print(df.isnull().sum())

# Optional: Save to file
df.describe().to_csv("results/merged_profile.csv")
