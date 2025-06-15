import json
import os

class Config:
    def __init__(self, config_file="config.json"):
        # Adjust path to read config.json from the root folder
        config_path = os.path.join(os.path.dirname(__file__), "..", config_file)

        # Load configuration file
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def get_url(self, endpoint, **kwargs):
        """Constructs full API URL using base URL and endpoint path."""
        base_url = self.config.get("base_url", "")
        path = self.config.get("endpoints", {}).get(endpoint, "")
        return f"{base_url}{path}".format(**kwargs)

    def get_headers(self):
        """Returns request headers from the config file."""
        return self.config.get("headers", {})

# Create a global config instance
config = Config()