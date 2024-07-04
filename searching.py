import pymongo
from generate_embedding import generate_embedding

client = pymongo.MongoClient("mongodb+srv://lakshyaagrawal:Lakshya12@cluster0.suugkij.mongodb.net/")
db = client.sample_mflix
collection = db.movies

query = "imaginary characters from outer space at war"

async def find_similar_documents(query_embedding):
    try:
        # Query for similar documents.
        pipeline = [
            {
                '$vectorSearch': {
                    'queryVector': query_embedding,
                    'path': 'embedding',  # Field name containing embeddings
                    'numCandidates': 100,
                    'limit': 4,
                    'index': 'PlotSemanticSearch',  # Optional: Index name if specified
                }
            }
        ]

        documents = await list(collection.aggregate(pipeline).to_list(None))
        return documents
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def serching_text(query):
    query_embedding= generate_embedding(query)
    find_similar_documents(query_embedding)


serching_text(query)