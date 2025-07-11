# Task_04_Descriptive_Stats


# 2024 US Presidential Election: Social Media Descriptive Analysis

This project presents a complete descriptive statistics engine built using three approaches — **Pure Python**, **Pandas**, and **Polars** — to analyze social media datasets related to the 2024 U.S. Presidential election.

It explores:
- Facebook Ads
- Facebook Posts
- Twitter Posts

The objective is to produce reusable statistical summaries and identify trends in political communication, reach, and campaign strategy.

---

## Datasets Used

This project analyzes **three CSV files**:

1. `2024_fb_ads_president_scored_anon.csv`
2. `2024_fb_posts_president_scored_anon.csv`
3. `2024_tw_posts_president_scored_anon.csv`

> **Important:** These datasets are provided privately.  
> **Download link**: [Google Drive](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)  
> After downloading, place the files in the **same folder** as your scripts.

---

## ⚙Setup & Requirements

### Python Version
- Python 3.8 or higher recommended

### Required Packages

Install all dependencies using:

```bash
pip install pandas polars matplotlib seaborn
```

---

##  How to Run the Scripts

### 1. Pure Python Script
```bash
python script1_full_pure_python.py
```
- No libraries required
- Computes count, mean, min, max, std deviation
- Also includes group-by summaries (`page_id`, `ad_id`)

---

###  2. Pandas Script
```bash
python script2_pandas_analysis.py
```
- Uses `DataFrame.describe()`, `value_counts()`, `nunique()`
- Easy, fast, and readable

---

###  3. Polars Script
```bash
python script3_polars_analysis.py
```
- Blazing fast performance
- Memory-efficient, ideal for large files

---

###  4. Visualization Script (Optional Bonus)
```bash
python visualize_data.py
```
- Generates histograms, boxplots, and bar charts
- Outputs stored in:
  - `facebook_ads_plots/`
  - `facebook_posts_plots/`
  - `twitter_posts_plots/`

---

## Key Insights from the Analysis

### Facebook Ads
- A small number of `page_id`s account for a **disproportionate share of impressions and spend**.
- Most ads have modest budgets; a few ads have extremely high visibility.
- Frequent themes: **health**, **immigration**, **election integrity**.

### Facebook Posts
- Post engagement is **highly skewed** — a few posts go viral, most get minimal attention.
- Some non-sponsored posts still include sponsor metadata, suggesting campaign coordination.

### Twitter Posts
- Retweets and replies dominate — suggesting reactive or viral strategy.
- Topic indicators suggest strong focus on **governance**, **race**, and **foreign policy**.

---

## Project Highlights

- Pure Python version demonstrates deep control over data pipelines.
- Polars achieves best performance — highly recommended for production-scale pipelines.
- Code is modular and works with any well-structured CSV dataset.

---

## Folder Structure

```
.
├── script1_full_pure_python.py     # Pure Python stats
├── script2_pandas_analysis.py      # Pandas version
├── script3_polars_analysis.py      # Polars version
├── visualize_data.py               # Bonus visualization script
├── README.md                       # You're here!
```


