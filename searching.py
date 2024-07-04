import pymongo
from generate_embedding import generate_embedding

# MongoDB connection setup
client = pymongo.MongoClient("mongodb+srv://lakshyaagrawal:Lakshya12@cluster0.suugkij.mongodb.net/")
db = client.Ojas_database
collection = db.resume

# Example query
query = "space at war"

# Generate embedding vector for the query
query_embedding = generate_embedding(query)

# Define the aggregation pipeline
pipeline = [
    {
        "$vectorSearch": {
            "index": "Resume_index",
            "queryVector": query_embedding,
            "path": "embedding",
            "limit": 5,
            "numCandidates": 100
        }
    },
    {
        "$project": {
            "_id": 1,
            "Summery": 1,
            "embedding": 0,
            "score": { "$meta": "vectorSearchScore" } #vectorSearchScore searchScore
        }
    }
]

try:
    # Execute the aggregation pipeline and retrieve documents
    documents = list(collection.aggregate(pipeline))
    print(documents)

except Exception as e:
    print(f"An error occurred: {e}")
    # Handle the error appropriately (e.g., log, retry, etc.)

# async def find_similar_documents(query_embedding):
#     try:
#         pipeline = [{
#                 "$search": {
#                 "index": "default",
#                 "knnBeta": {
#                     "vector": query_embedding,
#                     "path": "plot_embedding",
#                     "k": 5
#                 }
#                 }
#             },
#             {
#                 "$project": {
#                 "_id": 0,
#                 "plot": 1,
#                 "title": 1,
#                 "score": { "$meta": "searchScore" }
#                 }
#             }
#         ]

#         documents = await collection.aggregate(pipeline).to_list(None)
#         return documents

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None


# async def searching_text(query):  # Changed to async function to correctly await find_similar_documents
#     query_embedding = generate_embedding(query)
#     print(query_embedding)
#     return await find_similar_documents(query_embedding)  # Await find_similar_documents coroutine


# query = "space at war"
# result = await searching_text(query)  # Correctly await searching_text coroutine

# print(result)  # Do something with the result returned by find_similar_documents
