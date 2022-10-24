
from deepClassifier.utils import *
from deepClassifier.utils import read_yaml
from deepClassifier.constants import *
from deepClassifier.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH

    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories(["artifacts/data_ingestion"])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source = config.source,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config