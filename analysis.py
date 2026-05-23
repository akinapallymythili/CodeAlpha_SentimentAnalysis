import pandas as pd
from textblob import TextBlob

df = pd.read_csv("Amazon_Reviews.csv", encoding="latin1", nrows=1000)

print(df.columns)

df = df[["Review Text"]]

df.dropna(inplace=True)

df["Review Text"] = df["Review Text"].astype(str).str.lower()

def get_sentiment(text):
    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return "Positive"

    elif analysis.sentiment.polarity < 0:
        return "Negative"

    else:
        return "Neutral"


df["Sentiment"] = df["Review Text"].apply(get_sentiment)

print(df.head())

df.to_csv("Sentiment_Output.csv", index=False)

print("Analysis Completed Successfully")