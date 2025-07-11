import pandas as pd
import os
from time import perf_counter

# -------------- Helper Functions ----------------

def analyze_dataset_with_pandas(file_path, dataset_name):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    print(f"\n====== Analyzing {dataset_name} with Pandas ======\n")
    
    start = perf_counter()
    df = pd.read_csv(file_path)
    end = perf_counter()

    print(f"Loaded dataset in {round(end - start, 2)} seconds")
    print(f" Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    # Numerical summary
    print("===  Numeric Summary (describe) ===\n")
    print(df.describe(include='number').T)

    # Categorical summary
    print("\n=== Categorical Summary ===\n")
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols[:5]:  # limit to 5 columns for brevity
        print(f"Column: {col}")
        print(f"  Unique values: {df[col].nunique()}")
        print(f"  Top value: {df[col].value_counts(dropna=False).idxmax()}")
        print(f"  Frequency: {df[col].value_counts(dropna=False).max()}")
        print("-" * 50)

# -------------- Main Execution ----------------

if __name__ == "__main__":
    dataset_paths = {
         "Facebook Ads": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_ads_president_scored_anon.csv", 
        "Facebook Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_posts_president_scored_anon.csv",
        "Twitter Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_tw_posts_president_scored_anon.csv"
    }

    for name, path in dataset_paths.items():
        analyze_dataset_with_pandas(path, name)
