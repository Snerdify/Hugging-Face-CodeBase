from transformers import pipeline


# pipeline() is used across many tasks like text classification,
# text generation 


# here we are training it for sentiment analysis


classifier = pipeline("sentiment-analysis")

result = classifier("I am happy")
print(result)

