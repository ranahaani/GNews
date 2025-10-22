from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        try:
            self.analyzer = pipeline("sentiment-analysis")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.analyzer = None

    def analyze(self, text):
        if not self.analyzer:
            return {"label": "UNKNOWN", "score": 0.0}
        try:
            result = self.analyzer(text[:512])[0]  # Limit to first 512 chars
            return {"label": result['label'], "score": float(result['score'])}
        except Exception as e:
            print(f"Error analyzing text: {e}")
            return {"label": "ERROR", "score": 0.0}

    def analyze_batch(self, texts):
        return [self.analyze(text) for text in texts]
