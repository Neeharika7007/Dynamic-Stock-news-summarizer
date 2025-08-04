from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.05:
        sentiment = "Positive"
    elif polarity < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity
if __name__ == "__main__":
    text = input("Enter a headline: ")
    sentiment, score = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}, Score: {score:.2f}")







