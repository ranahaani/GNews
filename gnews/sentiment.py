from transformers import pipeline

# Load a lightweight sentiment analysis model (DistilBERT)
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """
    Analyze sentiment of a single text.
    Returns: dict with 'sentiment' (positive/negative/neutral) and 'sentiment_score'
    """
    if not text:
        return {"sentiment": "neutral", "sentiment_score": 0.0}
    
    result = sentiment_analyzer(text[:512])[0]  # limit text to 512 tokens for performance
    return {"sentiment": result["label"].lower(), "sentiment_score": float(result["score"])}

def analyze_sentiment_batch(text_list):
    """
    Analyze sentiment of multiple texts at once.
    Returns: list of sentiment dicts
    """
    return [analyze_sentiment(text) for text in text_list]

# Example usage
if __name__ == "__main__":
    sample_texts = [
        "Artificial intelligence is transforming the world!",
        "Stock markets crashed today due to global tensions.",
        "Weather is okay, nothing special."
    ]
    
    results = analyze_sentiment_batch(sample_texts)
    for text, sentiment in zip(sample_texts, results):
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment['sentiment']} | Score: {sentiment['sentiment_score']}\n")
