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


class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join( training_pipeline_config.artifact_dir, training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir, training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )

class DataTransformationConfig:
    def __init__(self,training_pipeline_config:training_pipeline):
        self.data_transformation_dir: str = os.path.join( training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME )
        self.transformed_train_file_path: str = os.path.join( self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TRAIN_FILE_NAME.replace("csv", "npy"),)
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,  training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TEST_FILE_NAME.replace("csv", "npy"), )
        self.transformed_object_file_path: str = os.path.join( self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME,)
