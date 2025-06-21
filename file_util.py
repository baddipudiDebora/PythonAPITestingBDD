import os
import json

def load_json_payload(file_name, folder='jsonSamples'):
    file_path = os.path.join(os.path.dirname(__file__), folder, f"{file_name}.json")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"🚫 File '{file_path}' not found. Please check the filename or path.")

    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"⚠️ Failed to parse JSON from '{file_path}': {e}")