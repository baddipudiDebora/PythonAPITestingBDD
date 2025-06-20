import json

import requests
from Config import config  # Import config module



def get_url(endpoint_name, pet_id=None):
    # Load configuration file
    with open("config.json", "r") as file:
        config = json.load(file)

    base_url = config["base_url"]
    endpoint_path = config["endpoints"].get(endpoint_name)

    if not endpoint_path:
        raise ValueError(f"Invalid endpoint name: {endpoint_name}")

    # Replace {pet_id} if needed
    if "{pet_id}" in endpoint_path and pet_id:
        print(pet_id)
        endpoint_path =endpoint_path.replace("{pet_id}", str(pet_id))

    return f"{base_url}{endpoint_path}"

def get_headers():
    """Retrieve headers"""
    headers = config.get_headers()
    headers["accept"] = "application/json"
    headers["Content-Type"]="application/x-www-form-urlencoded"
    return config.get_headers()

def send_request(api_verb, url, headers):
    """Send API request based on the verb"""
    if api_verb.lower() == "get":
        return requests.get(url, headers=headers)
    elif api_verb.lower() == "post":
        return requests.post(url, headers=get_post_headers())
    else:
        raise ValueError(f"Unsupported API verb: {api_verb}")


def get_post_headers():
    """Retrieve headers"""
    return {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
