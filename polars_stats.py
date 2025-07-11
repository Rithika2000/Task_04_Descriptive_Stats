import polars as pl
import os
from time import perf_counter

# -------------- Helper Functions ----------------

def analyze_dataset_with_polars(file_path, dataset_name):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"\n====== Analyzing {dataset_name} with Polars ======\n")

    start = perf_counter()
    df = pl.read_csv(file_path)
    end = perf_counter()

    print(f"Loaded dataset in {round(end - start, 2)} seconds")
    print(f" Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    # Numeric Summary
    print("=== Numeric Summary (describe) ===\n")
    print(df.describe())

    # Categorical Summary
    print("\n=== Categorical Summary ===\n")
    cat_cols = [col for col in df.columns if df[col].dtype == pl.Utf8]
    for col in cat_cols[:5]:  # limit to 5 for brevity
        print(f"Column: {col}")
        print(f"  Unique values: {df[col].n_unique()}")
        vc = df[col].value_counts()
        most_common = vc.sort("count", descending=True).row(0)
        print(f"  Top value: {most_common[0]}")
        print(f"  Frequency: {most_common[1]}")
        print("-" * 50)

# -------------- Main Execution ----------------

if __name__ == "__main__":
    dataset_paths = {
         "Facebook Ads": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_ads_president_scored_anon.csv", 
        "Facebook Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_posts_president_scored_anon.csv",
        "Twitter Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_tw_posts_president_scored_anon.csv"
    }

    for name, path in dataset_paths.items():
        analyze_dataset_with_polars(path, name)
