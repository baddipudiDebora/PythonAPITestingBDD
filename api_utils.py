import json
import requests
from Config import config  # Assumed to be a local module with get_headers()
from file_util import load_json_payload


def setup_context_for_endpoint(context, api_verb,  endpointname):
    context.api_verb =   api_verb
    url = get_url(endpointname)
    context.url = url
    context.base_url = url


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

    if api_verb in ("get","delete"):
        return requests.get(url, headers=headers)
    elif api_verb in ("post","put"):
        return requests.post(url, json=jsondata, headers=headers)
    else:
        raise ValueError(f"Unsupported API verb: {api_verb}")


def log_request_context(context):
    print(f"\n📡 API Verb: {getattr(context, 'api_verb', 'N/A')}")
    print(f"🌍 URL: {getattr(context, 'url', 'N/A')}")
    print(f"🧾 Headers: {getattr(context, 'headers', {})}")
    print(f"📦 Payload: {getattr(context, 'json_data', {})}\n")


def send_request_for_context(context):
    if context.api_verb.upper() in ("POST", "PUT"):
        context.response = send_request(api_verb=context.api_verb,url=context.url,headers=context.headers,jsondata=context.json_data)
    elif context.api_verb.upper() in ("GET", "DELETE"):
        context.response = send_request(api_verb=context.api_verb,url=context.url,headers=context.headers)
    else:
        raise RuntimeError("Not a valid API verb")
    if not hasattr(context, "response"):
        raise RuntimeError("Response not found. Ensure the request step runs before this step.")
    return None

def logResponse_context(context):
    print(f"🔢 Status Code: {context.response.status_code}")
    print(f"📋 Headers: {context.response.headers}")

    try:
        print(f"📦 JSON Response: {context.response.json()}")
    except Exception as e:
        print(f"❗ Response is not JSON: {context.response.text}")


def parse_value(value):
    try:
        # Try converting strings like "true", "123", or lists/objects into Python types
        return json.loads(value)
    except (json.JSONDecodeError, TypeError):
        return value  # Fall back to raw string if it can't be parsed


def load_and_override_json(jsonfileName, override_table, folder='jsonSamples'):
    payload = load_json_payload(jsonfileName, folder)

    for row in override_table:
        field = row['field'] if 'field' in row.headings else row[0]
        raw_value = row['value'] if 'value' in row.headings else row[1]
        value = parse_value(raw_value)

        if '.' in field:
            keys = field.split('.')
            ref = payload
            for i, key in enumerate(keys):
                key = int(key) if key.isdigit() else key
                if i == len(keys) - 1:
                    ref[key] = value
                else:
                    ref = ref[key]
        else:
            payload[field] = value

    return payload