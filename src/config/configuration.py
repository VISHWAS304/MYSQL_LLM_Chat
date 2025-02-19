from src.utils.common import read_yaml
from src.entity.config_entity import DatabaseConfig
from src.constants.constants import CONFIG_FILE_PATH
from pathlib import Path

class ConfigurationManager:
    def __init__(self):
        """
        Initialize the ConfigurationManager by loading the YAML configuration.
        """
        self.config = read_yaml(CONFIG_FILE_PATH)

    def get_database_config(self) -> DatabaseConfig:
        """
        Get the database configuration from the YAML file.

        Returns:
            DatabaseConfig: Database configuration as a dataclass object.
        """
        db_config = self.config["database"]
        return DatabaseConfig(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database_name=db_config["database_name"]
        )