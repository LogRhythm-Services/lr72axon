import argparse
import glob
import os
import sys
import urllib.parse
from enum import auto
from typing import List

import torch
from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from lr72axon.axon.models import *
from lr72axon.logrhythm7.models import *
from lr72axon.utils.list_utils import search_axon_list, create_axon_list_payload, create_axon_lists
from lr72axon.utils.mapping import *
from lr72axon.utils.utils import *


class ConversionMode(Enum):
    USE_NLP = auto()
    USE_TFIDF = auto()
    USE_DEFAULT = auto()


def create_axon_common_event_TFIDF(query_string: str, threshold=.1) -> list:
    all_subclasses = []
    for parent in axon_common_events:
        for subclass in parent['subclasses']:
            all_subclasses.append({
                'parent_guid': parent['guid'],
                'name': subclass['name'],
                'description': subclass['description'],
                'combined': f"{subclass['name']} {subclass['description']}",
                'guid': subclass['guid']  # Ensure 'guid' key exists
            })

    combined_strings = [entry['combined'] for entry in all_subclasses]
    combined_strings.append(query_string)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(combined_strings)
    cosine_similarities = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1]).flatten()

    max_similarity = max(cosine_similarities)
    if max_similarity >= threshold:
        max_index = cosine_similarities.argmax()
        best_match = all_subclasses[max_index]
        return [best_match['guid'], best_match['parent_guid']]

    return axon_default_common_event


def create_axon_common_event_npl(query, threshold=0.1):
    model = SentenceTransformer('all-mpnet-base-v2')

    all_subclasses = []
    for parent in axon_common_events:
        for subclass in parent['subclasses']:
            all_subclasses.append({
                'parent_guid': parent['guid'],
                'name': subclass['name'],
                'description': subclass['description'],
                'guid': subclass['guid'],
                'combined': f"{subclass['name']} {subclass['description']}"
            })

    subclass_texts = [entry['combined'] for entry in all_subclasses]
    subclass_embeddings = model.encode(subclass_texts, convert_to_tensor=True)
    query_embedding = model.encode([query], convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(query_embedding, subclass_embeddings)[0]

    max_score, max_idx = torch.max(cosine_scores, dim=0)

    if max_score.item() >= threshold:
        best_match = all_subclasses[max_idx.item()]
        return [best_match['guid'], best_match['parent_guid']]

    return axon_default_common_event


def search_on_axon_cache(list_name: str) -> list | None:
    return [item for item in list_ids_cache if item.get('lr7_name') == list_name]


def process_aie_list_to_axon_list(criteria: list[str]):
    global list_ids_cache
    global must_create_list
    new_criteria = []
    attributes = []
    sublist_array = []

    for item in criteria:
        match = re.match(r'(.+?) ((not )?in) SUBLIST_(.*)', item)
        if match:
            attribute = match.group(1)
            operator = match.group(2)
            list_information = match.group(4)

            attributes.append(attribute)
            sublist_array.append(list_information)
            list_parts = list_information.split('_')
            if len(list_parts) < 2:
                log_message(logger, 'error', f"Invalid SUBLIST format: {list_information}")
                pass

            guid = list_parts[0]
            name = list_parts[1]

            axon_lists = search_on_axon_cache(name)

            if not axon_lists or len(axon_lists) < 1:
                axon_lists = search_axon_list(name, axon_api_key, tenant_id=axon_tenant_id, logger=logger, debug=True)

            if not axon_lists and must_create_list:
                axon_payloads = create_axon_list_payload(name, logrhythm_api_key, list_guid=guid,
                                                         base_url=logrhythm_url,
                                                         logger=logger, exclude_types=exclude_lr_list_types)
                created_lists = create_axon_lists(axon_payloads, axon_api_key, tenant_id=axon_tenant_id)
                if created_lists:
                    for created_list in created_lists:
                        created_list['lr7_name'] = name
                        list_ids_cache.append(created_list)
                        axon_lists.append(created_list)

                if not axon_lists or len(axon_lists) < 1:
                    log_message(logger, 'error', f"List {name} not found nor able to create in Axon.")
                    log_message(logger, 'info', f"Returning same list for manual process")
                    pass

            if axon_lists and len(axon_lists) > 0:
                log_message(logger, 'info', f"List {name} found or created in Axon, expanding now.")
                n_criteria_list = [f"{attribute} {operator} LIST;{axon_list['id']};{axon_list['column_id']}"
                                   for axon_list in axon_lists]
                if len(n_criteria_list) > 2:
                    n_criteria = f"({' or '.join(n_criteria_list)})"
                else:
                    n_criteria = f"{' or '.join(n_criteria_list)}"
                new_criteria.append({item: n_criteria})

    if len(new_criteria) > 0:
        log_message(logger, 'info', f"Returning new criteria: {new_criteria}")
        return new_criteria
    else:
        log_message(logger, 'info', f"Returning same list for manual process")
        return None


def create_axon_filter_from_aieCriteria(primary_criteria: list[Criteria], filter_in: list[Criteria],
                                        filter_out: list[Criteria], observer=True, unattribute=True) -> str:
    primary_strings = []
    primary_lists = []
    filter_in_strings = []
    filter_in_lists = []
    filter_out_strings = []
    filter_out_lists = []

    for criteria in primary_criteria:
        str_part, list_part = criteria.create_filter_for_axon_mapping(observer, unattribute)
        primary_strings.append(str_part)
        primary_lists.extend(list_part)

    for criteria in filter_in:
        str_part, list_part = criteria.create_filter_for_axon_mapping(observer, unattribute)
        filter_in_strings.append(str_part)
        filter_in_lists.extend(list_part)

    for criteria in filter_out:
        str_part, list_part = criteria.create_filter_for_axon_mapping(observer, unattribute)
        filter_out_strings.append(str_part)
        filter_out_lists.extend(list_part)

    primary_lists = list(set(primary_lists))
    filter_in_lists = list(set(filter_in_lists))
    filter_out_lists = list(set(filter_out_lists))

    primary_string = " and ".join(primary_strings)
    filter_in_string = " and ".join(filter_in_strings)
    filter_out_string = " and ".join(filter_out_strings)

    axon_filter = ""
    if primary_string:
        axon_filter += primary_string
    if filter_in_string:
        axon_filter += f" and ({filter_in_string})" if axon_filter else filter_in_string
    if filter_out_string:
        axon_filter += f" and not ({filter_out_string})" if axon_filter else f"not ({filter_out_string})"

    if not axon_filter.strip():
        axon_filter = "general_information.common_event_name contains contains anything"

    if len(primary_lists) > 0:
        new_filters = process_aie_list_to_axon_list(primary_lists)
        if new_filters:
            for new_filter in new_filters:
                for key, new_value in new_filter.items():
                    axon_filter = axon_filter.replace(key, new_value)

    if len(filter_in_lists) > 0:
        new_filters = process_aie_list_to_axon_list(filter_in_lists)
        if new_filters:
            for new_filter in new_filters:
                for key, new_value in new_filter.items():
                    axon_filter = axon_filter.replace(key, new_value)

    if len(filter_out_lists) > 0:
        new_filters = process_aie_list_to_axon_list(filter_out_lists)
        if new_filters:
            for new_filter in new_filters:
                for key, new_value in new_filter.items():
                    axon_filter = axon_filter.replace(key, new_value)

    return axon_filter


def create_axon_operations(aie_rule: AIERule, observer=True, unattribute=True) -> list[Operation] | None:
    operations: List[Operation] = []
    for i, aie_block in enumerate(aie_rule.blocks):
        filter = create_axon_filter_from_aieCriteria(aie_block.primaryCriteria, aie_block.filterIn,
                                                     aie_block.filterOut, observer, unattribute)

        if aie_block.blockType.name == "LogObserved":
            observed = LogObserved(filter=filter, groupByFields=aie_block.get_list_group_by_fields_for_axon())
            axon_operation = Operation("WHERE_PATTERN_OPERATION",
                                       blockType="LOG_OBSERVED",
                                       ruleElementKey=str(uuid.uuid4()),
                                       logObserved=observed)
            operations.append(axon_operation)

        elif aie_block.blockType.name == "ThresholdObserved":
            threshold_str = aie_block.thresholdFields[0].value
            threshold_value = int(float(threshold_str))

            duration_str = aie_block.durationSeconds
            duration_value = int(float(duration_str))

            threshold = CountThresholdObserved(filter=filter,
                                               threshold=threshold_value,
                                               groupByFields=aie_block.get_list_group_by_fields_for_axon(),
                                               windowSeconds=duration_value)
            axon_operation = Operation("WHERE_PATTERN_OPERATION",
                                       blockType="COUNT_THRESHOLD_OBSERVED",
                                       ruleElementKey=str(uuid.uuid4()),
                                       countThresholdObserved=threshold)
            operations.append(axon_operation)
        elif aie_block.blockType.name == "UniqueValuesObserved":
            threshold_str = aie_block.values[0].count
            threshold_value = int(float(threshold_str))

            unique_values = CountUniqueValuesObserved(filter=filter,
                                                      threshold=threshold_value,
                                                      groupByFields=aie_block.get_list_group_by_fields_for_axon(),
                                                      windowSeconds=aie_block.durationSeconds,
                                                      uniqueValueFields=aie_block.get_list_unique_fields_for_axon())
            axon_operation = Operation("WHERE_PATTERN_OPERATION",
                                       blockType="COUNT_UNIQUE_VALUES_OBSERVED",
                                       ruleElementKey=str(uuid.uuid4()),
                                       countUniqueValuesObserved=unique_values)
            operations.append(axon_operation)
        else:
            pass

        if len(aie_rule.blocks) > 1:
            if i < len(aie_rule.blocks) - 1:
                axon_relation = Operation("FOLLOWED_BY_PATTERN_OPERATION",
                                          ruleElementKey=str(uuid.uuid4()))
                operations.append(axon_relation)
            else:
                seconds_str = aie_block.blockRelationship.duration
                seconds_value = int(float(seconds_str) / 1000)
                axon_relation = Operation("WITHIN_PATTERN_OPERATION",
                                          ruleElementKey=str(uuid.uuid4()),
                                          seconds=seconds_value)
                operations.append(axon_relation)

    return operations


def create_axon_metadata_fields(common_event: CommonEvent) -> dict:
    if 0 <= common_event.riskRating <= 3:
        severity = "low"
    elif 4 <= common_event.riskRating <= 6:
        severity = "medium"
    else:
        severity = "high"
    metadata_fields = {
        "threat.severity": severity,
    }

    return metadata_fields


def convert_aie_rule_to_axon_rule(aierule: AIERule,
                                  mode: ConversionMode = ConversionMode.USE_DEFAULT,
                                  observed=True, unattribute=True, logger=None) -> AxonRule | None:
    if not aierule:
        log_message(logger, 'error', "AIE Rule is None.")
        return None
    for aie_block in aierule.blocks:
        if not is_supported_block_type(aie_block.blockType.name):
            log_message(logger, 'error',
                        f"Block type {aie_block.blockType.name} - {aie_block.blockType.id} "
                        f"is not supported, skipping AIE rule {aierule.name}")
            return None

    axon_rule = AxonRule(aierule.name, aierule.description)
    if mode == ConversionMode.USE_NLP:
        axon_common_events = create_axon_common_event_npl(aierule.name)
    elif mode == ConversionMode.USE_TFIDF:
        axon_common_events = create_axon_common_event_TFIDF(aierule.name)
    else:
        axon_common_events = axon_default_common_event

    axon_operations = create_axon_operations(aierule, observer=observed, unattribute=unattribute)
    axon_pattern = Pattern(axon_operations)
    axon_metadata_fields = create_axon_metadata_fields(aierule.commonEvent)
    axon_observation_pipeline = ObservationPipeline(axon_pattern, axon_common_events,
                                                    metadataFields=axon_metadata_fields)

    axon_rule.observationPipeline = axon_observation_pipeline
    axon_supression = SuppressionConfig.from_milliseconds(aierule.supression,
                                                          aierule.blocks[0].get_list_group_by_fields_for_axon())
    axon_rule.observationPipeline.suppressionConfig = axon_supression

    return axon_rule


def get_aie_rule_definition(air_rule_id: int, api_key: str, base_url: str = "http://127.0.0.1:8505",
                            logger=None) -> AIERule | None:
    lr_api_url = urllib.parse.urljoin(base_url, f'/lr-services-host-api/actions/domainobject')
    lr_headers = build_auth_headers(api_key, is_axon=False)
    lr_services_host_payload = {
        'source': '',
        'destination': "DomainObjectService",
        'messageType': "GetObjectRequest",
        'ver': 1,
        'data': {
            'objectType': "AieRule",
            'userId': 1,
            'objectId': str(air_rule_id)
        }
    }
    try:
        aie_json_rule = make_api_request('POST', lr_api_url, lr_headers, data=lr_services_host_payload)
        aie_rule = AIERule.from_dict(aie_json_rule)
    except Exception:
        log_message(logger, 'error', f"Rule ID {air_rule_id} was not found in the AIE Rule definition.")
        return None
    return aie_rule


def get_aie_rule_from_json_file(json_file_path: str, logger=None) -> AIERule | None:
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
            rule_object = create_dict_from_json(json_data)
            aie_rule = AIERule.from_dict(rule_object)
            return aie_rule
    except FileNotFoundError:
        log_message(logger, 'error', f"File not found: {json_file_path}")
        return None
    except Exception as e:
        log_message(logger, 'error', f"Error reading AIE Rule from file: {e}")
        return None


def expand_ranges(input_string, logger=None) -> list[int]:
    results = []
    elements = input_string.split(",")
    for element in elements:
        try:
            element = element.strip()
            if "-" in element:
                start, end = map(str.strip, element.split("-"))
                results.extend(range(int(start), int(end) + 1))
            else:
                results.append(int(element))
        except ValueError:
            log_message(logger, 'error', f"Invalid range: {element}")
        except Exception as e:
            log_message(logger, 'error', f"Generic Error expanding ranges: {e}")
    return results


def save_axon_rule_to_file(axon_rule_object: AxonRule, directory, filename, logger=None):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            log_message(logger, 'error', f"Error creating directory: {e}")
            return

    file_path = os.path.join(directory, f"{os.path.basename(filename)}")

    try:
        axon_rule_json_str = str(axon_rule_object)

        with open(file_path, 'w') as file:
            file.write(axon_rule_json_str)

        log_message(logger, 'info', f"Successfully saved Axon rule {axon_rule_object.title} to {file_path}")

    except IOError as e:
        log_message(logger, 'error', f"Error saving Axon rule to file: {e}")


conversion_mode_map = {
    "default": ConversionMode.USE_DEFAULT,
    "nlp": ConversionMode.USE_NLP,
    "vector": ConversionMode.USE_TFIDF
}


# Global variables to be used in the conversion process
logrhythm_api_key = ""
axon_api_key = ""
axon_tenant_id = ""
axon_url = ""
list_ids_cache = []
logger = None
must_create_list = True
logrhythm_url = ""


def conversion_cli():
    global logrhythm_api_key
    global logrhythm_url
    global axon_api_key
    global axon_tenant_id
    global axon_url
    global logger
    global must_create_list

    parser = argparse.ArgumentParser(description="CLI tool converting AIE Rules into Axon Rules")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Specify a single rule file to process.", metavar="FILE")
    group.add_argument("-d", "--directory",
                       help="Specify a directory containing the JSON exported AIERules", metavar="DIRECTORY")
    group.add_argument("-a", "--api", action="store_true",
                       help="Establish API Mode to gather the AIE Rule from LR API directly")

    parser.add_argument("--ids",
                        help="Comma-separated list of rule IDs or ranges e.g., '1,2,4-6' Only valid with -a/--api.",
                        metavar="RULEID")
    parser.add_argument("--lr-url", help="Base URL for the LogRhythm7 API", default="http://127.0.0.1:8505")
    parser.add_argument("--lr-api-key", help="API key for authentication", metavar="APIKEY", required=True)

    parser.add_argument("-x", "--create", help="Create the Axon List if it does not exist", action="store_true")
    parser.add_argument("--axon-api-key", help="Axon API Key", required=True)
    parser.add_argument("--tenant-id", help="Axon Tenant ID", default="lrtraining")
    parser.add_argument("--axon-url", help="Base URL for the Axon API", default="https://api.na01.prod.boreas.cloud")

    parser.add_argument("-c", "--conversion-mode", choices=['default', 'nlp', 'vector'],
                        default="default", help="Specify the conversion mode. Can be 'default', 'nlp', or 'vector'. "
                                                "Default is 'default'. Selecting nlp or vector may impact performance.")

    parser.add_argument("-O", "--output-directory", default="c:\\LogRhythm\\AxonRules",
                        help="Specify an output directory. Default is c:\\LogRhythm\\AxonRules.", metavar="DIRECTORY")
    parser.add_argument("-o", "--skip-observables", action="store_true",
                        help="Skip processing of observables.")
    parser.add_argument("-u", "--skip-unattributed", action="store_true",
                        help="Skip processing of unattributed entities.")

    args = parser.parse_args()

    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory)

    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    info_handler = logging.FileHandler('aie2axon_converted.log')
    error_file_handler = logging.FileHandler('aie2axon_non_converted.log')

    console_handler.setLevel(logging.INFO)
    info_handler.setLevel(logging.INFO)
    info_handler.addFilter(InfoFilter())
    error_file_handler.setLevel(logging.ERROR)

    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(log_format)
    info_handler.setFormatter(log_format)
    error_file_handler.setFormatter(log_format)

    _logger.addHandler(console_handler)
    _logger.addHandler(info_handler)
    _logger.addHandler(error_file_handler)

    logger = _logger

    selected_mode_str = args.conversion_mode
    selected_mode = conversion_mode_map[selected_mode_str]

    logrhythm_api_key = args.lr_api_key
    logrhythm_url = args.lr_url
    axon_api_key = args.axon_api_key
    axon_tenant_id = args.tenant_id
    axon_url = args.axon_url
    must_create_list = args.create

    if args.api:
        if not args.ids:
            parser.error("--api requires --ids to be specified.")

    if args.file:
        aie_rule = get_aie_rule_from_json_file(args.file)
        axon_rule = convert_aie_rule_to_axon_rule(aie_rule, observed=not args.skip_observables,
                                                  unattribute=not args.skip_unattributed, mode=selected_mode,
                                                  logger=_logger)
        if axon_rule is not None:
            save_axon_rule_to_file(axon_rule, args.output_directory, args.file, logger=_logger)
            _logger.info(f"Successfully conversion for  AIE rule {aie_rule.name}")

    elif args.directory:
        json_files = glob.glob(os.path.join(args.directory, "*.json"))
        for file_path in json_files:
            aie_rule = get_aie_rule_from_json_file(file_path)
            axon_rule = convert_aie_rule_to_axon_rule(aie_rule,
                                                      observed=not args.skip_observables,
                                                      unattribute=not args.skip_unattributed, mode=selected_mode,
                                                      logger=_logger)
            if axon_rule is not None:
                save_axon_rule_to_file(axon_rule, args.output_directory, file_path, logger=_logger)
                _logger.info(f"Successfully conversion for  AIE rule {aie_rule.name}")
    elif args.api is not None:
        numbers = expand_ranges(args.ids)
        for number in numbers:
            aie_rule = get_aie_rule_definition(number, logrhythm_api_key, logger=logger)

            if aie_rule is not None:
                axon_rule = convert_aie_rule_to_axon_rule(aie_rule, observed=not args.skip_observables,
                                                          unattribute=not args.skip_unattributed, mode=selected_mode,
                                                          logger=_logger)
                if axon_rule is not None:
                    save_axon_rule_to_file(axon_rule, args.output_directory,
                                           f"{number} - {sanitize_filename(axon_rule.title)}.json",
                                           logger=_logger)
                    _logger.info(f"Successfully conversion for  AIE rule {aie_rule.name}")


if __name__ == "__main__":
    conversion_cli()
