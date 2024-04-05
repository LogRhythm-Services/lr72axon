import ipaddress
import os
import urllib.parse
from collections import defaultdict

from lr72axon.axon.models import ListColumn, ListDefinition, ListItem, AxonListPayload, ListColumnType
from lr72axon.utils.utils import build_auth_headers, make_api_request, sanitize_filename, log_message
from lr72axon.utils.mapping import exclude_lr_list_types, axon_list_types_mapping


def get_lr7_list_summary(list_name: str, api_key: str, base_url: str = "http://127.0.0.1:8505",
                         logger=None, max_items: int = 10000000, exclude_types: list[str] = None) -> dict | None:
    lr_headers = build_auth_headers(api_key, is_axon=False,
                                    additional_headers={'name': list_name, 'MaxItemsThreshold': str(max_items)})
    list_api_url = urllib.parse.urljoin(base_url, '/lr-admin-api/lists')

    try:
        list_summary = make_api_request('GET', list_api_url, lr_headers)
        if not list_summary:
            log_message(logger, 'error', 'List summary is empty.')
            return None

        if exclude_types:
            list_description = next(
                (list_item for list_item in list_summary if list_item['listType'] not in exclude_types), None)
            if list_description is None:
                log_message(logger, 'error', 'Unsupported list type.')
            return list_description

        log_message(logger, 'error', 'Unsupported list type.')
        return None

    except Exception as e:
        log_message(logger, 'error', f'Unexpected error while fetching list: {e}')
        return None


def get_lr7_list(list_guid: str, api_key: str, base_url: str = "http://127.0.0.1:8505",
                 logger=None, max_items: int = 10000000) -> list | None:
    lr_headers = build_auth_headers(api_key, is_axon=False,
                                    additional_headers={'MaxItemsThreshold': str(max_items)})
    items_api_url = urllib.parse.urljoin(base_url, f'/lr-admin-api/lists/{list_guid}')

    try:
        list_items_response = make_api_request('GET', items_api_url, lr_headers, check_status=False)
        if list_items_response.status_code != 200:
            log_message(logger, 'error',
                        f'Error fetching list items, status code: {list_items_response.status_code}')
            return None

        list_items = list_items_response.json().get('items')
        if list_items is None:
            # log_message(logger, 'error', 'No items found in the list.')
            return None

        return list_items

    except Exception as e:
        log_message(logger, 'error', f'Unexpected error while fetching list: {e}')
        return None


def get_all_lr7_lists(api_key: str, base_url: str = "http://127.0.0.1:8505", logger=None,
                      pageSize: int = 10000000, exclude_types: list[str] = None) -> list | None:
    lr_headers = build_auth_headers(api_key, is_axon=False,
                                    additional_headers={'pageSize': str(pageSize)})
    list_api_url = urllib.parse.urljoin(base_url, '/lr-admin-api/lists')
    try:
        lr_all_lists_response = make_api_request('GET', list_api_url, lr_headers, check_status=False)
        if lr_all_lists_response.status_code != 200:
            log_message(logger, 'error',
                        f'Error fetching list items, status code: {lr_all_lists_response.status_code}')
            return None

        lr_all_lists = lr_all_lists_response.json()
        if not lr_all_lists:
            log_message(logger, 'error', 'List summary is empty.')
            return None

        if not exclude_types:
            return lr_all_lists

        filtered_list = [lr_list for lr_list in lr_all_lists if lr_list['listType'] not in exclude_types]

        return filtered_list

    except Exception as e:
        log_message(logger, 'error', f'Unexpected error while fetching list: {e}')
        return None


def convert_sql_wildcard(lr_list_items: list) -> list:
    transformed_values = []
    for item in lr_list_items:
        if item.get('isPattern'):
            transformed_value = item['value'].replace('%', '*')
        else:
            transformed_value = item['value']
        transformed_values.append(transformed_value)

    return transformed_values


def expand_port_range(port_range: str) -> list:
    if ',' in port_range:
        start_port, end_port = port_range.split(',')
        return list(range(int(start_port), int(end_port) + 1))
    else:
        return [int(port_range)]


def expand_ip_range(ip_range_str):
    start_ip_str, end_ip_str = ip_range_str.split(',')

    start_ip = int(ipaddress.IPv4Address(start_ip_str))
    end_ip = int(ipaddress.IPv4Address(end_ip_str))

    ip_list = [str(ipaddress.IPv4Address(ip)) for ip in range(start_ip, end_ip + 1)]

    return ip_list


def get_lists_by_list_type(list_items):
    expanded_items = []
    for item in list_items:
        if item['listItemDataType'] == 'IPRange':
            expanded_range = expand_ip_range(item['value'])
            for ip in expanded_range:
                expanded_items.append({
                    "isPattern": False,
                    "listItemDataType": "IP",
                    "value": ip,
                    "listItemType": "IP"
                })
        elif item['listItemDataType'] == 'PortRange':
            expanded_range = expand_port_range(item['value'])
            for port in expanded_range:
                expanded_items.append({
                    "isPattern": False,
                    "listItemDataType": "Int32",
                    "value": str(port),
                    "listItemType": "Port"
                })
        elif item['listItemDataType'] == 'String':
            transformed_values = convert_sql_wildcard([item])
            for value in transformed_values:
                expanded_items.append({
                    "isPattern": False,
                    "listItemDataType": "String",
                    "value": value,
                    "listItemType": item.get('listItemType', 'String')
                })
        else:
            expanded_items.append(item)

    grouped_items = defaultdict(list)
    for item in expanded_items:
        grouped_items[item['listItemDataType']].append(item)

    return grouped_items


def process_list_item_type(list_guid: str, api_key: str, base_url: str = "http://127.0.0.1:8505", logger=None,
                           max_items: int = 10000000, exclude_types: list[str] = None, collected_items=None,
                           list_name=None):
    if collected_items is None:
        collected_items = []
    name_part = f' - Name: {list_name}' if list_name else ''
    log_message(logger, 'info', f"Processing list: {list_guid}{name_part}")
    list_items = get_lr7_list(list_guid, api_key, base_url, logger, max_items=max_items)

    if list_items is None:
        log_message(logger, 'error', f'No items found for GUID {list_guid}{name_part}.')
        return collected_items

    for item in list_items:
        if item.get('listItemDataType') != "List":
            collected_items.append(item)
        else:
            nested_guid = item.get('valueAsListReference', {}).get('guid')
            if nested_guid:
                log_message(logger, 'info',
                            f"Processing nested list: {nested_guid} from item: {item.get('valueAsListReference', {}).get('name')}")
                process_list_item_type(nested_guid, api_key, base_url, logger,
                                       exclude_types=exclude_types, collected_items=collected_items)
            else:
                log_message(logger, 'warning', f"Missing 'valueAsListReference.guid' for item in list: {list_guid}")

    return collected_items


def create_axon_list_payload(list_name: str, api_key: str, list_guid: str = None, base_url: str = "http://127.0.0.1:8505",
                             logger=None, exclude_types: list[str] = None) -> list[AxonListPayload] | None:
    axon_payloads = []
    list_summary = None
    if not list_guid:
        list_summary = get_lr7_list_summary(list_name, api_key, base_url, logger, exclude_types=exclude_types)
        if not list_summary or 'guid' not in list_summary:
            log_message(logger, 'error', f'Failed to retrieve list summary for {list_name}.')
            return None
        lr_list_guid = list_summary['guid']
    else:
        lr_list_guid = list_guid

    all_lr_list_items = process_list_item_type(lr_list_guid, api_key, base_url,
                                               exclude_types=exclude_lr_list_types, list_name=list_name, logger=logger)
    lr_grouped_lists = get_lists_by_list_type(all_lr_list_items)

    num_item_types = len(lr_grouped_lists.keys())
    for item_type, sublist in lr_grouped_lists.items():
        if sublist:
            list_item_type = sublist[0].get('listItemType', 'Unknown')
            if num_item_types == 1:
                unique_name = f"{list_name}"
            else:
                unique_name = f"{list_name} - {list_item_type}"
            axon_column = ListColumn(list_item_type, list_item_type, axon_list_types_mapping[item_type])
            axon_column_id = axon_column.id
            if not list_guid:
                short_description = list_summary.get('shortDescription', f"Converted {unique_name} from LR7")
            else:
                short_description = f"Converted {unique_name} from LR7"
            axon_list_definition = ListDefinition(unique_name, short_description, [axon_column])

            axon_column_values = []

            for item in sublist:
                item_value = item.get('value')
                axon_item = ListItem(axon_column_id, item_value)
                axon_column_values.append(axon_item)
                pass

            axon_payload = AxonListPayload(axon_list_definition, axon_column_values)
            axon_payloads.append(axon_payload)

    return axon_payloads


def create_axon_lists(payload: list[AxonListPayload], api_key: str, tenant_id: str = "demo",
                      base_url: str = "https://api.na01.prod.boreas.cloud/", logger=None, debug=False):
    axon_headers = build_auth_headers(api_key, is_axon=True)
    axon_list_api_url = urllib.parse.urljoin(base_url, f'/list-svc/v1/tenants/{tenant_id}/lists')

    lists_created = []

    for axon_payload in payload:
        axon_dict_payload = axon_payload.to_dict()
        try:
            response = make_api_request('POST', axon_list_api_url, axon_headers, data=axon_dict_payload,
                                        check_status=False)
            if response.status_code != 201 or response.status_code != 200:
                log_message(logger, 'error', f'Error creating list: {response.status_code}')
                if debug:
                    log_message(logger, 'error', f'Error creating list: {response.text}')
            else:
                axon_list_created = response.json()
                list_created = {
                    'id': axon_list_created['content']['listDefinition']['id'],
                    'title': axon_list_created['content']['listDefinition']['title'],
                    'column_id': axon_list_created['content']['listDefinition']['columns'][0]['id']
                }
                log_message(logger, 'info', f"List created successfully: {response.status_code}")
                lists_created.append(list_created)

        except Exception as e:
            log_message(logger, 'error', f"Unexpected error while creating list: {e}")

    return lists_created


def search_axon_list(list_name: str, api_key: str, tenant_id: str = "demo", limit=10000,
                     base_url: str = "https://api.na01.prod.boreas.cloud/", logger=None, debug=False):
    axon_lists_for_name = []
    axon_api_url = urllib.parse.urljoin(base_url,
                                        f'/list-svc/v1/tenants/{tenant_id}/list-definitions/byColumnTypeAndTitlePattern')

    axon_headers = build_auth_headers(api_key, is_axon=True)
    for column_type in ListColumnType:
        params = {
            'limit': limit,
            'titlePattern': f'{list_name}%',
            'columnType': column_type.value
        }
        try:
            if debug:
                log_message(logger, 'info', f"Searching for Axon list: {list_name} and type: {column_type.value}")
            axon_response = make_api_request('GET', axon_api_url, axon_headers, check_status=False, parameters=params)
            if axon_response.status_code == 200 or axon_response.status_code == 201:
                axon_list = axon_response.json()
                if not isinstance(axon_list, list):
                    axon_list = [axon_list]

                axon_lists_for_name.extend(axon_list)

        except Exception as e:
            log_message(logger, 'error', f"Error searching for Axon list: {e}")

    filtered_and_transformed = [
        {
            "orig_name": list_name,
            "id": item["id"],
            "title": item["title"],
            "column_id": item["columns"][0]["id"] if item.get("columns") else None
        }
        for axon_obj in axon_lists_for_name if "content" in axon_obj and axon_obj["content"]
        for item in axon_obj["content"]
    ]

    return filtered_and_transformed


def save_axon_list_to_file(axon_lists_payload: list[AxonListPayload], directory, filename, logger=None):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            log_message(logger, 'error', f"Error creating directory: {e}")
            return

    for i, axon_payload in enumerate(axon_lists_payload, start=1):
        sanitize_file = sanitize_filename(filename)
        file_path = os.path.join(directory, f"{sanitize_file} - {i}")
        axon_payload_str = str(axon_payload)
        try:
            with open(file_path, 'w') as file:
                file.write(axon_payload_str)

            log_message(logger, 'info', f"Successfully saved Axon rule to {file_path}")

        except IOError as e:
            log_message(logger, 'error', f"Error saving Axon rule to file: {e}")
