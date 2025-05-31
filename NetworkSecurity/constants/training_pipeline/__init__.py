import os 
import sys 
import numpy as np 
import pandas as pd 

## Data Injestion Constants

TARGET_COLUMN = "Result"
PIPELINE_NAME : str = "NetworkSecurity"
ARTIFACT_DIR:str= "Artifacts"
FILE_NAME :str="phisingData.csv"
TRAIN_FILE_NAME:str= "train.csv"
TEST_FILE_NAME:str= "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

 ## Data Injestion Constants

DATA_INJESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INJESTION_DATABASE_NAME:str = "Siddhant"
DATA_INJESTION_DIR_NAME:str = "data_injestion"
DATA_INJESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INJESTION_INJESTED_DIR:str="injested"
DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO:float= 0.2

## Data Validation Constants 

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

## Data Transformation Constants 

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"

