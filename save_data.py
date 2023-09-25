import pymongo
import scraper

def save(ls_dict, collection_name):
    # MongoDB connection information
    mongo_uri = "mongodb+srv://moksud:Sylhet3100@cluster0.2jzvkyv.mongodb.net/?retryWrites=true&w=majority"  # Change to your MongoDB URI if necessary
    db_name = "dse"  # Change to your database name if necessary
   # collection_name = "stocks"  # Change to your collection name if necessary

    # Sample document with the specified schema
    document = {
        "SL": "",
        "TRADING_CODE": "",
        "LTP": "",
        "HIGH": "",
        "LOW": "",
        "CLOSE": "",
        "YCP": "",
        "CHANGE": "",
        "TRADE": "",
        "VALUE": "",
        "VOLUME": ""
    }

    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]


    # Iterate through the data in ls_dict and update existing documents or insert new ones
    for item in ls_dict:
        trading_code = item["TRADING_CODE"]
        
        # Search for an existing document with the same trading code
        existing_document = collection.find_one({"TRADING_CODE": trading_code})
        
        if existing_document:
            # Update the existing document
            collection.update_one({"_id": existing_document["_id"]}, {"$set": item})
        else:
            # Insert a new document
            collection.insert_one(item)

    # Close the MongoDB connection
    client.close()

    print("Data updated or inserted into MongoDB collection.")
    # Close the MongoDB connection

