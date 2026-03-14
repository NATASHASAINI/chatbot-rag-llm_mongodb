from sentence_transformers import SentenceTransformer
from pymongo import MongoClient

model = SentenceTransformer("all-MiniLM-L6-v2")

client = MongoClient("mongodb://localhost:27017/")
db = client["rag_chatbot"]
collection = db["documents"]

def embed(text):
    return model.encode(text).tolist()

def search(query):
    query_vector = embed(query)

    results = collection.find()

    docs = []
    for r in results:
        docs.append(r["text"])

    return docs

query = input("Ask something: ")
print(search(query))

