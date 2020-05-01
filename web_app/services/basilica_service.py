import basilica
import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
# print(type(connection)) #> <class 'basilica.Connection'>

# print(embedding)
# a list of 768 numbers?
if __name__ == "__main__":
    embedding = connection.embed_sentence("hey this is a cool tweet", model="twitter")
    tweets = ["Hello world", "artificial intelligence", "another tweet"]
    embeddings = connection.embed_sentences(tweets, model="twitter")
    for embed in embeddings:
        print("-----")
        print(len(embed))