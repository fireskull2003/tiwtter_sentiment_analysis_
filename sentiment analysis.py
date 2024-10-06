import pandas as pd 
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('task 1/Tweets.csv')
print(df.columns)

def clean_text(text):
    text = text.lower()  
    return text

df['cleaned_post'] = df['text'].apply(clean_text)

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

df['sentiment'] = df['cleaned_post'].apply(get_sentiment)

def classify_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment_label'] = df['sentiment'].apply(classify_sentiment)

print(df[['text', 'sentiment_label']])

sentiment_counts = df['sentiment_label'].value_counts()
print("\nSentiment Distribution:")
print(sentiment_counts)

plt.figure(figsize=(8, 6))
sns.countplot(x='sentiment_label', data=df, palette='Set2')
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

