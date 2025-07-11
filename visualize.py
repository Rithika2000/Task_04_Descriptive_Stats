import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set seaborn style
sns.set(style="whitegrid")

def visualize_dataset(file_path, dataset_name, max_plots=3):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"\n Generating visualizations for {dataset_name}...\n")
    df = pd.read_csv(file_path)

    numeric_cols = df.select_dtypes(include="number").columns
    cat_cols = df.select_dtypes(include="object").columns

    # Create output directory
    output_dir = f"{dataset_name.lower().replace(' ', '_')}_plots"
    os.makedirs(output_dir, exist_ok=True)

    # Plot histograms and boxplots for numeric columns
    for col in numeric_cols[:max_plots]:
        plt.figure(figsize=(10, 4))
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f"{col} - Histogram")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{col}_histogram.png")
        plt.show()

        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[col].dropna())
        plt.title(f"{col} - Boxplot")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{col}_boxplot.png")
        plt.show()

    # Bar charts for top categorical values
    for col in cat_cols[:max_plots]:
        plt.figure(figsize=(10, 5))
        top_values = df[col].value_counts().head(10)
        sns.barplot(
            x=top_values.values,
            y=top_values.index,
            hue=top_values.index,
            palette="viridis",
            legend=False
        )
        plt.title(f"{col} - Top 10 Categories")
        plt.xlabel("Frequency")
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{col}_barplot.png")
        plt.show()

    print(f"Saved visualizations to folder: {output_dir}")

# ---------------- Main Execution ----------------

if __name__ == "__main__":
    dataset_paths = {
          "Facebook Ads": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_ads_president_scored_anon.csv", 
        "Facebook Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_posts_president_scored_anon.csv",
        "Twitter Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_tw_posts_president_scored_anon.csv"
    }

    for name, path in dataset_paths.items():
        visualize_dataset(path, name)
