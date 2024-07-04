import pymongo
from generate_embedding import generate_embedding
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://lakshyaagrawal:Lakshya12@cluster0.suugkij.mongodb.net/")

## database 
db = client.Ojas_database
# collection = db['sample_mflix']  # Replace 'my_collection' with your desired collection name

## table 
collection = db.resume

Summery_text = '''Skills/Relevant Coursework
•Taken electives: Microeconomics, Macroeconomics, Data Science, Financial Economics, Financial Analytics
•Coursera: Financial Markets, Private Equity through courses from Wharton, Yale and IESE Business School
•CFA Investment Foundations Programme: Scored above 85% in the final exam, first in IIT Patna
Co-curricular Achievements
•Finished in National Top 20 among1100+teams in Business Quiz and Economics Case Study at IIMI.
 Percentage: 96.4 %) 2008 - 2018
Internship Experience
•Quantitative Research Consultant |WorldQuant Research India Mumbai, India
Mentorship of Mr. Dmitry Peysakhovich, WorldQuant Armenia Office Jul 2023 - Apr 2024
◦Achieved 292ndrankversus30K globally in Stage 2 (Final) of International Quant Championship ’22.
◦Created proprietary models with 16.5% returns and2.5% turnover in US and China equity markets.
 CPI: 8.45 ) 2020 - 2024 (Expected)
•DGET Junior College of Science Thane, India
(Maharashtra HSC conducted by MSBHSCE.'''



embedding_Data = generate_embedding(Summery_text)
now = datetime.now()

# Prepare document to insert into collection

document = {
    'Summery': Summery_text,
    'embedding': embedding_Data,
    "data": now
}


# # Insert a document into the collection
insert_result = collection.insert_one(document)

print(f"Inserted document id: {insert_result.inserted_id}")

# Close MongoDB connection
client.close()
