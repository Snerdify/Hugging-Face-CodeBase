# pipeline () is used to abstarct away most of the code

from transformers import pipeline



# we can do the same thing for text generation , only here we are specifying which model we are going to use
generator = pipeline("text-generation", model ="distilgpt2")

result = generator ( "In this chapter we are going to learn how to",  max_length = 30, num_return_sequences = 2,)


print(result)
