from datetime import datetime 
import os
from networksecurity.constants import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name, timestamp)
        self.timestamp: str=timestamp


class DataIngestionCongif:
    def __init__(self, training_pileline_config:TrainingPipelineConfig):
        self.data_ingestion_dir: str=os.path.join(
            training_pileline_config.artifact_dir,training_pileline_config.DATA_INGESTION_CONFIG
        )

        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_DIR_NAME, training_pipeline.FILE_NAME
        )

        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_DIR_NAME, training_pipeline.TRAIN_FILE_NAME
        )
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_DIR_NAME, training_pipeline.TEST_FILE_NAME
        )
        self.train_test_spilt_ratio: float =training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION 
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME

