from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return result['label'].lower()

if __name__ == "__main__":
    user_text = input("Enter your mood description: ")
    print("Detected emotion:", analyze_sentiment(user_text))
