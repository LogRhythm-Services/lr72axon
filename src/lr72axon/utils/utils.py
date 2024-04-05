import logging
import re
import requests


class InfoFilter(logging.Filter):
    def filter(self, record):
        # Only allow INFO level messages
        return record.levelno == logging.INFO


def check_response_status(response, expected_statuses):
    if response.status_code not in expected_statuses:
        raise Exception(f'API Request replied with an invalid Response Code: {response.status_code}')


def make_api_request(method, url, headers, data=None, verify=False, check_status=True, parameters=None):
    response = requests.request(method, url, headers=headers, json=data, verify=verify, params=parameters)
    if check_status:
        check_response_status(response, {200, 201})
        return response.json()
    else:
        return response


def build_auth_headers(api_key, is_axon=False, additional_headers=None):
    headers = {
        "Authorization": f"Bearer {api_key}" if not is_axon else api_key,
        **({"Content-Type": "application/json"} if is_axon else {})
    }
    if additional_headers:
        headers.update(additional_headers)
    return headers


def create_dict_from_json(json_data):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, (dict, list)):
                json_data[key] = create_dict_from_json(value)
        return json_data
    elif isinstance(json_data, list):
        return [create_dict_from_json(item) for item in json_data]
    else:
        return json_data


def sanitize_filename(filename):
    filename = filename.replace(" ", "_")
    sanitized_filename = re.sub(r'[^\w\d_]', '', filename)
    return sanitized_filename


def log_message(logger, level, message):
    if logger is not None:
        if level == 'info':
            logger.info(message)
        elif level == 'error':
            logger.error(message)
    else:
        print(message)
