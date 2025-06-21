import json
import requests
from Config import config  # Assumed to be a local module with get_headers()

def get_url(endpoint_name, pet_id=None):
    """Builds the full URL for a given API endpoint."""
    with open("config.json", "r") as file:
        config_data = json.load(file)

    base_url = config_data["base_url"]
    endpoint_path = config_data["endpoints"].get(endpoint_name)

    if not endpoint_path:
        raise ValueError(f"Invalid endpoint name: {endpoint_name}")

    if "{pet_id}" in endpoint_path and pet_id:
        endpoint_path = endpoint_path.replace("{pet_id}", str(pet_id))

    return f"{base_url}{endpoint_path}"


def get_headers(context):
    """Retrieve headers from config and ensure necessary defaults are included."""
    headers = config.get_headers()
    if context.api_verb.upper() == "GET":
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer your_token_here"
        }
    elif context.api_verb.upper() == "POST":
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    return headers


def send_request(api_verb, url, headers=None, jsondata=None):
    """Send API request based on the HTTP verb."""
    api_verb = api_verb.lower()

    if api_verb == "get":
        return requests.get(url, headers=headers)
    elif api_verb == "post":
        return requests.post(url, json=jsondata, headers=headers)
    else:
        raise ValueError(f"Unsupported API verb: {api_verb}")


def log_request_context(context):
    print(f"\n📡 API Verb: {getattr(context, 'api_verb', 'N/A')}")
    print(f"🌍 URL: {getattr(context, 'url', 'N/A')}")
    print(f"🧾 Headers: {getattr(context, 'headers', {})}")
    print(f"📦 Payload: {getattr(context, 'json_data', {})}\n")