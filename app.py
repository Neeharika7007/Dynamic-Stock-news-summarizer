from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import streamlit as st
from stock_data import fetch_stock_data
from news_handler import fetch_news
from sentiment import analyze_sentiment
# 📦 Imports (at the very top of app.py)
import pandas as pd
from sklearn.model_selection import train_test_split

# 📁 Load dataset from /data folder
df = pd.read_csv("data/your_data.csv")  # Keep your dataset in 'data/' folder

# 🛠️ Prepare features and target
X = df.drop("target_column", axis=1)
y = df["target_column"]

# ✂️ Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 🎯 App Title
st.title("📈 Stock Trend & Sentiment Dashboard")
st.subheader("💬 Analyze Custom Headline Sentiment")

custom_headline = st.text_input("Enter any news headline to test its sentiment")

if custom_headline:
    sentiment, score = analyze_sentiment(custom_headline)
    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Polarity Score:** {score:.2f}")


# 📥 User Input for stock ticker
ticker = st.text_input("Enter Stock Ticker (e.g. AAPL, TSLA, RELIANCE.NS)")

# 🛠 Only run if a ticker is provided
if ticker:
    # Step 1: Get stock data
    st.subheader(f"📊 Stock Price for {ticker}")
    data = fetch_stock_data(ticker, "2024-06-01", "2024-07-01")
    st.line_chart(data["Close"])  # plot closing prices

    # Step 2: Get related news
    st.subheader("📰 Recent News Articles")
    articles = fetch_news(ticker)

    for article in articles:
        title = article.get("title", "No Title")
        source = article.get("source", {}).get("name", "Unknown")
        url = article.get("url", "#")

        # Step 3: Analyze sentiment
        sentiment, score = analyze_sentiment(title)

        # Step 4: Display in Streamlit
        st.markdown(f"**{title}**")
        st.write(f"Source: {source}")
        st.write(f"Sentiment: {sentiment} ({score:.2f})")
        st.write(f"[Read more]({url})")
        st.write("---")
        # 💬 Analyze Custom Headline Sentiment
st.subheader("💬 Test Your Own News Headline")

custom_headline = st.text_input("Enter a news headline")

if custom_headline:
    sentiment, score = analyze_sentiment(custom_headline)

    st.write("### 🧠 Sentiment Analysis Result")
    st.markdown(f"**Headline**: {custom_headline}")
    st.markdown(f"**Sentiment**: `{sentiment}`")
    st.markdown(f"**Polarity Score**: `{score:.2f}`")


    # Optional emojis for extra flair
    emoji = {"Positive": "✅", "Negative": "⚠️", "Neutral": "😐"}
    st.markdown(f"**Mood Emoji**: {emoji.get(sentiment, '❓')}")
    st.subheader("📊 Compare Two Headlines")

headline1 = st.text_input("Enter Headline 1")
headline2 = st.text_input("Enter Headline 2")

if headline1 and headline2:
    sentiment1, score1 = analyze_sentiment(headline1)
    sentiment2, score2 = analyze_sentiment(headline2)

    st.markdown("### 🧠 Sentiment Results")



    st.write(f"**Headline 1:** {headline1}")
    st.write(f"Sentiment: {sentiment1}")
    st.write(f"Polarity Score: {score1:.2f}")
    st.write("---")
    st.write(f"**Headline 2:** {headline2}")
    st.write(f"Sentiment: {sentiment2}")
    st.write(f"Polarity Score: {score2:.2f}")
    st.write("---")

    difference = abs(score1 - score2)
    st.markdown(f"### 📐 Difference in Polarity Score: `{difference:.2f}`")
    st.subheader("📉 ROC Curve & AUC Score")

fpr, tpr, thresholds = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)

fig, ax = plt.subplots()
ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
ax.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('Receiver Operating Characteristic')
ax.legend(loc="lower right")

st.pyplot(fig)



