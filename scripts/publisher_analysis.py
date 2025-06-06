import pandas as pd

def analyze_publishers(df):
    print("Top Publishers:")
    print(df["publisher"].value_counts().head())

def extract_email_domains(df):
    if "publisher" in df.columns:
        df["domain"] = df["publisher"].str.extract(r'@(.+)$')
        print("Top Domains:")
        print(df["domain"].value_counts().head())

if __name__ == "__main__":
    df = pd.read_csv("data/raw_analyst_ratings.csv")
    analyze_publishers(df)
    extract_email_domains(df)
