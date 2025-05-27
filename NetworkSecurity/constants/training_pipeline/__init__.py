import os 
import sys 
import numpy as np 
import pandas as pd 


TARGET_COLUMN = "Result"
PIPELINE_NAME : str = "NetworkSecurity"
ARTIFACT_DIR:str= "Artifacts"
FILE_NAME :str="phisingData.csv"
TRAIN_FILE_NAME:str= "train.csv"
TEST_FILE_NAME:str= "test.csv"



DATA_INJESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INJESTION_DATABASE_NAME:str = "Siddhant"
DATA_INJESTION_DIR_NAME:str = "data_injestion"
DATA_INJESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INJESTION_INJESTED_DIR:str="injested"
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO:float= 0.2