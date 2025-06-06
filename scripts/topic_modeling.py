import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def perform_topic_modeling(df, n_topics=5):
    # Drop missing and lowercase text
    df["headline"] = df["headline"].dropna().str.lower()
    
    # Vectorize
    vectorizer = CountVectorizer(max_df=0.9, min_df=1, stop_words='english')
    dtm = vectorizer.fit_transform(df["headline"])
    
    # LDA
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(dtm)
    
    # Display topics
    for idx, topic in enumerate(lda.components_):
        top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
        print(f"Topic #{idx + 1}: {', '.join(top_words)}")

if __name__ == "__main__":
    df = pd.read_csv("data/raw_analyst_ratings.csv")
    print("Columns in dataset:", df.columns.tolist())  # Optional sanity check
    perform_topic_modeling(df)
