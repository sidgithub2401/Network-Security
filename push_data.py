import os 
import sys 
import json
import certifi
import pandas as pd
import numpy as np 
import pymongo
import pymongo.mongo_client
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging import logger
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

print(MONGO_DB_URL)

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self,file_path):            ### Converting the csv into Json Format and returning the records in the form of list
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e :
            raise NetworkSecurityException(e,sys)

    def insert_data_mongo(self,records,database,collection):  ## Inserting Data into the MogoDB 
        try:  
             self.records = records
             self.database = database
             self.collection = collection
             self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)  ## Create the MONGO CLIENT to connect with Database 

             self.database = self.mongo_client[self.database]
             
             self.collection = self.database[self.collection]

             self.collection.insert_many(self.records)
             return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__== '__main__':
    FILE_PATH = "NetworkData\phisingData.csv"
    obj = NetworkDataExtract()
    records = obj.csv_to_json(file_path=FILE_PATH)
    print(records)
    no_records = obj.insert_data_mongo(records=records,database="Siddhant",collection="NetworkData")    
    print(no_records)