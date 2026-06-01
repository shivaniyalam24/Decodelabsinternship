from textblob import TextBlob

print("=== Text Recognition System ===")

text = input("Enter a sentence: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

if polarity > 0:
    sentiment = "Positive 😊"
elif polarity < 0:
    sentiment = "Negative 😔"
else:
    sentiment = "Neutral 😐"

print("\nResults:")
print("Text:", text)
print("Sentiment:", sentiment)
print("Polarity Score:", polarity)