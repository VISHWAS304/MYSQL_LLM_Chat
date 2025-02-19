from dataclasses import dataclass
from pathlib import Path
from typing import Dict

@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    user: str
    password: str
    database_name: str