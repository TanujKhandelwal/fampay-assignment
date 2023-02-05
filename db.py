import pymongo
from constants import MONGO_CONNECTION_URL

def get_db_obj():
  #connection to mongodb
  try:
    source_client = pymongo.MongoClient(MONGO_CONNECTION_URL)
    models = source_client.get_database('models')
    return models
  except Exception as e:
    print("Could not connect to mongodb", e)
  return None