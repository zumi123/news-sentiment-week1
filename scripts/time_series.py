import pandas as pd
import matplotlib.pyplot as plt

def analyze_publication_dates(df):
    # Convert all date strings to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True)
    
    # Drop rows where conversion failed
    df = df.dropna(subset=["date"])
    
    # Normalize to date only (optional)
    df["date_only"] = df["date"].dt.date
    
    # Count and plot
    trend = df["date_only"].value_counts().sort_index()
    trend.plot(kind="line", title="Article Publication Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/raw_analyst_ratings.csv")
    analyze_publication_dates(df)
