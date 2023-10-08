from transformers import pipeline

# here we are going to use pipeline to to find the value of masked words

# filled mask pipeline is pre training objective of BERT

unmasker = pipeline("fill-mask")
result =unmasker("I have a <mask> dog" , top_k=2)

print(result)

# more tasks that you can perform
'''
Translation- 
Summarizing a large document using summarizer pipeline
Question answering 
zero-shot-classification
automatic speech recognition
'''