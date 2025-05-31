from NetworkSecurity.components.data_injestion import DataIngestion
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataInjestionConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
from NetworkSecurity.entity.config_entity import DataValidationConfig
from NetworkSecurity.components.data_validation import DataValidation
from NetworkSecurity.entity.artifact_entity import DataValidationArtifact
from NetworkSecurity.entity.config_entity import DataTransformationConfig
from NetworkSecurity.entity.artifact_entity import DataTransformationArtifact
from NetworkSecurity.components.data_transformation import DataTransformation
import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataInjestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")

    except Exception as e:
        raise NetworkSecurityException(e,sys)
