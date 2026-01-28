from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception .exception import NetworkSecurityException
from networksecurity.logging_utils.logger import logging
from networksecurity.entity.config_entity import DataIngestionCongif
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        trainingPipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionCongif(trainingPipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)
        raise NetworkSecurityException(e) from e