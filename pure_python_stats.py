import csv
import math
from collections import defaultdict, Counter
from time import perf_counter
import os

# ------------------- Helper Functions -------------------

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def compute_statistics(column_data):
    stats = {}
    cleaned_data = [x for x in column_data if x not in ('', 'NA', 'NaN', None)]
    numeric_data = [float(x) for x in cleaned_data if is_float(x)]

    stats['count'] = len(cleaned_data)

    if numeric_data:
        stats['mean'] = sum(numeric_data) / len(numeric_data)
        stats['min'] = min(numeric_data)
        stats['max'] = max(numeric_data)
        if len(numeric_data) > 1:
            mean = stats['mean']
            stats['std_dev'] = math.sqrt(sum((x - mean) ** 2 for x in numeric_data) / (len(numeric_data) - 1))
        else:
            stats['std_dev'] = 0.0
    else:
        value_counts = Counter(cleaned_data)
        stats['unique_values'] = len(value_counts)
        stats['most_frequent'] = value_counts.most_common(1)[0] if value_counts else None

    return stats

def analyze_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        columns = defaultdict(list)

        for row in reader:
            for key, value in row.items():
                columns[key.strip()].append(value.strip() if value else '')

    summary = {}
    for col, data in columns.items():
        summary[col] = compute_statistics(data)

    return summary

def group_and_analyze(rows, group_keys):
    grouped = defaultdict(lambda: defaultdict(list))

    for row in rows:
        group_id = tuple(row[k] for k in group_keys if k in row)
        for col, val in row.items():
            grouped[group_id][col].append(val)

    result = {}
    for group_id, columns in grouped.items():
        result[group_id] = {col: compute_statistics(data) for col, data in columns.items()}

    return result

def analyze_csv_with_grouping(file_path, group_keys):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = [dict((k.strip(), v.strip()) for k, v in row.items()) for row in reader]

    return group_and_analyze(rows, group_keys)

# ------------------- Main Execution -------------------

if __name__ == "__main__":
    # === Part A: Unaggregated Stats for All 3 Datasets ===
    dataset_paths = {
        "Facebook Ads": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_ads_president_scored_anon.csv", 
        "Facebook Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_posts_president_scored_anon.csv",
        "Twitter Posts": "/Users/rithikagurram/Documents/OPT Work/period_03/2024_tw_posts_president_scored_anon.csv"
    }

    for name, path in dataset_paths.items():
        print(f"\n====== [Part A] Analyzing {name} Dataset ======\n")
        if not os.path.exists(path):
            print(f"File not found: {path}. Please make sure it's in your folder.\n")
            continue

        start = perf_counter()
        result = analyze_csv(path)
        end = perf_counter()
        print(f"Execution Time: {round(end - start, 2)} seconds\n")

        for col, stats in result.items():
            print(f"Column: {col}")
            for stat_name, val in stats.items():
                print(f"  {stat_name}: {val}")
            print("-" * 50)

    # === Part B: Grouped Stats for Facebook Ads Dataset ===
    ads_path = "/Users/rithikagurram/Documents/OPT Work/period_03/2024_fb_ads_president_scored_anon.csv"

    if os.path.exists(ads_path):
        print(f"\n====== [Part B] Grouped Analysis for Facebook Ads Dataset ======\n")

        for group_keys in [["page_id"], ["page_id", "ad_id"]]:
            print(f"\n--- Grouped by {group_keys} ---\n")
            start = perf_counter()
            grouped_result = analyze_csv_with_grouping(ads_path, group_keys)
            end = perf_counter()
            print(f"Execution Time: {round(end - start, 2)} seconds")

            for group_id, col_stats in list(grouped_result.items())[:2]:  # show only 2 groups
                print(f"\nGroup: {group_id}")
                for col, stats in col_stats.items():
                    print(f"  Column: {col}")
                    for stat_name, val in stats.items():
                        print(f"    {stat_name}: {val}")
                    print("  ---")
    else:
        print("\n Facebook Ads file not found for Part B.")
