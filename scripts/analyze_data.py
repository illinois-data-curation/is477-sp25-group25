# analyze_data.py

#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_clean(path="results/cleaned_data.csv"):
    return pd.read_csv(path)

def describe(df):
    stats = df.describe().T
    stats.to_csv("results/descriptive_stats.csv")
    print("– Descriptive stats → results/descriptive_stats.csv")

def corr_heatmap(df):
    corr = df.corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig("results/correlation_matrix.png")
    plt.close()
    print("– Correlation heatmap → results/correlation_matrix.png")

def plot_trends(df):
    metrics = ["arrest_rate", "unemployment_rate"]
    for m in metrics:
        plt.figure()
        plt.plot(df["Year"], df[m], marker="o")
        plt.xlabel("Year")
        plt.ylabel(m.replace("_", " ").title())
        plt.title(f"{m.replace('_',' ').title()} Over Time")
        plt.tight_layout()
        out = f"results/{m}_trend.png"
        plt.savefig(out)
        plt.close()
        print(f"– Trend plot → {out}")

def main():
    df = load_clean()
    os.makedirs("results", exist_ok=True)
    describe(df)
    corr_heatmap(df)
    plot_trends(df)
    print("✅ Analysis complete.")

if __name__ == "__main__":
    main()