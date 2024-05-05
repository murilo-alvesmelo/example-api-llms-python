from transformers import pipeline

def get_sentiment_analysis(text):
    sentiment_analysis = pipeline("sentiment-analysis")
    result = sentiment_analysis(text)
    return result

