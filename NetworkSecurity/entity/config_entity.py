from datetime import datetime
import os 
from NetworkSecurity.constants import training_pipeline


class TrainingPipelineConfig:      ### Generic Information 
    def __init__(self,timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir= os.path.join(self.artifact_name,timestamp)
        self.timestamp:str = timestamp 
        


class DataInjestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.data_injestion_dir :str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INJESTION_DIR_NAME)     ## artifacts/data_injestion

        self.feature_store_path :str = os.path.join(self.data_injestion_dir, training_pipeline.DATA_INJESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME)    ## artifacts/data_injestion/feature_store/phising_data.csv

        self.training_file_path :str = os.path.join(self.data_injestion_dir,training_pipeline.DATA_INJESTION_INJESTED_DIR,training_pipeline.TRAIN_FILE_NAME)   ## artifacts/data_injestion/injested/train.csv

        self.testing_file_path :str = os.path.join(self.data_injestion_dir,training_pipeline.DATA_INJESTION_INJESTED_DIR,training_pipeline.TEST_FILE_NAME)     ## artifacts/data_injestion/injested/test.csv

        self.data_injestion_train_test_ratio : float = training_pipeline.DATA_INJESTION_TRAIN_TEST_SPLIT_RATIO

        self.data_injestion_database_name:str = training_pipeline.DATA_INJESTION_DATABASE_NAME

        self.data_injestion_collection_name:str = training_pipeline.DATA_INJESTION_COLLECTION_NAME