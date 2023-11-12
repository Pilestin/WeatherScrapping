
from pymongo import MongoClient


def get_collection(collection_name):
    """
    Verilen collection ismine göre collection'ı döndürür.

    """
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['weather']
        collection = db[collection_name]
        return collection
    except Exception as e:
        print("Get collection failed! Error: {}".format(e))
        return None

def insert_data_to_mongo(obj):
    """
    Verilen objeyi ilgili collection'a kaydeder.
    """
    try:
        collection = get_collection("weather")
        collection.insert_many(obj)
        
        
    except Exception as e:
        print(f"Veritabanına kayıt sırasında hata : {e}")