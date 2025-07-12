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

## Setup & Requirements

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
python pure_stats_python.py
```
- No libraries required
- Computes count, mean, min, max, std deviation
- Also includes group-by summaries (`page_id`, `ad_id`)

---

###  2. Pandas Script
```bash
python pandas_stats.py
```
- Uses `DataFrame.describe()`, `value_counts()`, `nunique()`
- Easy, fast, and readable

---

###  3. Polars Script
```bash
python polars_stats.py
```
- Blazing fast performance
- Memory-efficient, ideal for large files

---

###  4. Visualization Script (Optional Bonus)
```bash
python visualize.py
```
- Generates histograms, boxplots, and bar charts
- Outputs stored in:
  - `facebook_ads_plots/`
  - `facebook_posts_plots/`
  - `twitter_posts_plots/`

---

## Key Insights from the Analysis

### Facebook Ads

- **Ad Spend Distribution**: Majority of ads had low or no spend, while a few had very high budgets (over $46,000), indicating significant investment by key pages.
- **Impression Disparity**: Some ads reached over 20 million users, showing wide exposure inequality.
- **Campaign Themes**: Most common ad narratives included **health**, **governance**, **immigration**, and **election integrity**.
- **Targeted Delivery**: Presence of `delivery_by_region` and `demographic_distribution` confirms geo-demographic targeting.
- **Few Dominant Pages**: Group-by analysis showed that a limited number of pages controlled most ad distribution.
- **Ad Reuse**: Repeated `ad_id`s across different `page_id`s point to strategic reuse or A/B testing.

### Facebook Posts
- **Engagement Concentration**: Likes, shares, and comments are heavily skewed, with a few posts generating the bulk of interaction.
- **Emotional Reactions**: Variation in reactions (e.g., `Love`, `Haha`, `Angry`) reveals the emotional tone of content.
- **Sponsorship and Performance**: Sponsored posts generally outperform non-sponsored ones, as seen in `Overperforming Score`.
- **Video Content**: Posts with longer videos correlate with higher view counts.
- **Topic Focus**: Frequent themes include **governance**, **education**, and **immigration**.
- **Admin Location Insight**: Most pages are U.S.-based, but some show foreign administration, which could raise concerns over influence.

### Twitter Posts
- **Amplification Over Creation**: Many tweets are retweets or replies, showing Twitter’s role in **spreading** rather than **originating** content.
- **Extreme Engagement Skew**: Few tweets generate the most likes, replies, and retweets.
- **Key Topics**: Consistent focus on **race**, **governance**, and **foreign policy** throughout the dataset.
- **Reply Control Mechanism**: Use of `isConversationControlled` reflects attempts to manage public response.
- **Temporal Patterns**: Fields like `createdAt` and `month_year` could help identify engagement spikes during key political moments.

---

## Project Highlights

- Pure Python version demonstrates deep control over data pipelines.
- Polars achieves best performance — highly recommended for production-scale pipelines.
- Code is modular and works with any well-structured CSV dataset.

---

## Folder Structure

```
.
├── pure_stats_python.py    # Pure Python stats
├── pandas_stats.py      # Pandas version
├── polars_stats.py    # Polars version
├── visualize.py      # Bonus visualization script
├── README.md        # Documentation              
```


