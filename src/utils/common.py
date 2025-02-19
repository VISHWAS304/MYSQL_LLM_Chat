import yaml
from pathlib import Path

def read_yaml(file_path: Path) -> dict:
    """
    Read a YAML file and return its contents as a dictionary.

    Args:
        file_path (Path): Path to the YAML file.

    Returns:
        dict: Contents of the YAML file.
    """
    with open(file_path, "r") as file:
        return yaml.safe_load(file)