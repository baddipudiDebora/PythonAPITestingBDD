import json
import os

class Config:
    def __init__(self, config_file="config.json"):
        # Get the project's root directory
        root_path = os.path.abspath(os.path.dirname(__file__))  # Location of Config.py
        config_path = os.path.join(root_path, config_file)  # Expecting config.json in the same folder

        # Verify if the config file exists before attempting to load it
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")

        # Load configuration file
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def get_url(self, endpoint, **kwargs):
        base_url = self.config.get("base_url", "")
        path = self.config.get("endpoints", {}).get(endpoint, "")
        return f"{base_url}{path}".format(**kwargs)

    def get_headers(self):
        return self.config.get("headers", {})

# Create a global config instance
config = Config()

