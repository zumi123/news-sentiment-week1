import pandas as pd

def analyze_headlines(df):
    df["headline_length"] = df["headline"].str.len()
    print("Headline Length Stats:")
    print(df["headline_length"].describe())

def count_articles_per_publisher(df):
    print("Articles per Publisher:")
    print(df["publisher"].value_counts())

if __name__ == "__main__":
    df = pd.read_csv("data/raw_analyst_ratings.csv")
    analyze_headlines(df)
    count_articles_per_publisher(df)
