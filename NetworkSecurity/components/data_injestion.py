import pymongo.mongo_client
from NetworkSecurity.exception.exception import  NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.artifact_entity import DataInjestionArtifact
#### Importing the Data Injestion Config 
from NetworkSecurity.entity.config_entity import DataInjestionConfig
import os 
import sys
import pymongo
import pandas as pd
import numpy as np
from typing import List
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataInjestion:
    def __init__(self,data_injestion_config:DataInjestionConfig):
        try:
            self.data_injestion_config = data_injestion_config

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    
    def export_collection_to_dataframe(self):
        try:
            database_name = self.data_injestion_config.data_injestion_database_name
            collection_name = self.data_injestion_config.data_injestion_collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df.drop(columns=["_id"],axis=1)
            
            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise NetworkSecurityException(e,sys)



    
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path = self.data_injestion_config.feature_store_dir
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e,sys)



    def split_data_train_test_split(self,dataframe:pd.DataFrame):
        try:
            train_set , test_set  = train_test_split(dataframe,self.data_injestion_config.data_injestion_train_test_ratio)
            logging.info("Performed train test split on Dataframe")

            dir_name = self.data_injestion_config.training_file_path
            os.makedirs(dir_name,exist_ok=True)

            logging.info("Exporting train and test file path")

            train_set.to_csv(self.data_injestion_config.training_file_path,index=False,header = True)
            test_set.to_csv(self.data_injestion_config.testing_file_path,index=False,header = True)

            logging.info("Exported the train and test file")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    


    def initial_data_injestion(self):
        try:
            dataframe = self.export_collection_to_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_train_test_split(dataframe)
            data_injestion_artifact = DataInjestionArtifact(trained_file_path=self.data_injestion_config.training_file_path,test_file_path=self.data_injestion_config.testing_file_path)
            return data_injestion_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)