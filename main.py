from NetworkSecurity.components.data_injestion import DataInjestion
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from NetworkSecurity.entity.config_entity import DataInjestionConfig
from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_injestion_config = DataInjestionConfig(training_pipeline_config)
        data_injestion = DataInjestion(data_injestion_config)
        logging.info("Initial Data Injestion ")
        data_injestion_artifact = data_injestion.initial_data_injestion()
        print(data_injestion_artifact.trained_file_path)
        print(data_injestion_artifact.trained_file_path)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
