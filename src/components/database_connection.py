import pandas as pd
import pymysql
from src.entity.config_entity import DatabaseConfig

class DataBase:
    def __init__(self, db_config: DatabaseConfig):
        """
        Initialize the DataDumper with database configuration.

        Args:
            db_config (DatabaseConfig): Database configuration.
        """
        self.db_config = db_config

    def connect_to_database(self):
        """
        Connect to the MySQL database using the configuration.

        Returns:
            pymysql.connections.Connection: Database connection object.
        """
        return pymysql.connect(
            host=self.db_config.host,
            user=self.db_config.user,
            password=self.db_config.password,
            database=self.db_config.database_name
        )

