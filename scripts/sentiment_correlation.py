import os
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# === CONFIGURATION ===
NEWS_PATH = "data/raw_analyst_ratings.csv"
STOCK_PATH = "data/yfinance_data/AAPL_historical_data.csv"
OUTPUT_DIR = "outputs"
PLOT_PATH = os.path.join(OUTPUT_DIR, "sentiment_vs_return.png")

# === LOAD DATA ===
news_df = pd.read_csv(NEWS_PATH)
stock_df = pd.read_csv(STOCK_PATH)

# === DATE NORMALIZATION ===
news_df["date"] = pd.to_datetime(news_df["date"], errors="coerce", utc=True).dt.date
stock_df["Date"] = pd.to_datetime(stock_df["Date"]).dt.date

# === SENTIMENT ANALYSIS ===
def get_sentiment(text):
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0.0

news_df["sentiment"] = news_df["headline"].apply(get_sentiment)

# === AVERAGE DAILY SENTIMENT ===
daily_sentiment = news_df.groupby("date")["sentiment"].mean().reset_index()

# === CALCULATE DAILY STOCK RETURNS ===
stock_df["return"] = stock_df["Close"].pct_change()

# === MERGE DATASETS ===
merged_df = pd.merge(daily_sentiment, stock_df[["Date", "return"]], left_on="date", right_on="Date", how="inner")

# === CORRELATION ANALYSIS ===
correlation = merged_df["sentiment"].corr(merged_df["return"])

# === PLOT ===
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.figure(figsize=(10, 6))
plt.scatter(merged_df["sentiment"], merged_df["return"], alpha=0.7)
plt.title(f"Sentiment vs Stock Return (Correlation: {correlation:.4f})")
plt.xlabel("Average Daily Sentiment")
plt.ylabel("Daily Return")
plt.grid(True)
plt.tight_layout()
plt.savefig(PLOT_PATH)
print(f"Correlation: {correlation:.4f}")
print(f"Plot saved to: {PLOT_PATH}")
