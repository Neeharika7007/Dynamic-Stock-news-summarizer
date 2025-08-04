from sentiment import analyze_sentiment

# Choose a headline to test
headline = "Analyst With Sell Rating On AAPL Stock Warns Tim Cook's Company 'Is Unprepared For Something That Transformational'"

# Run sentiment analysis
sentiment, score = analyze_sentiment(headline)

# Show results
print("Headline:", headline)
print("Sentiment:", sentiment)
print("Polarity Score:", round(score, 2))
