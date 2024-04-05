import argparse
import logging
import sys
from lr72axon.utils.utils import InfoFilter
from lr72axon.utils.list_utils import *


def list_cli():
    parser = argparse.ArgumentParser(description="CLI tool converting LogRhythm7 Lists to Axon Lists")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-n", "--name", help="Specify The LogRhythm List to be Converted", metavar="FILE")
    group.add_argument("-a", "--all", help="Convert All LogRhythm Lists", action="store_true")
    group.add_argument("-s", "--search", help="Search for a List in Axon", metavar="SEARCH")

    parser.add_argument("--lr-api-key", help="LogRhythm API Key", required=True)
    parser.add_argument("--lr-url", help="Base URL for the API", default="http://127.0.0.1:8505")

    parser.add_argument("--axon-api-key", help="Axon API Key", required=True)
    parser.add_argument("--tenant-id", help="Axon Tenant ID", default="demo")
    parser.add_argument("--axon-url", help="Base URL for the API", default="https://api.na01.prod.boreas.cloud")

    parser.add_argument("-d", "--debug", help="Enable Debug Logging", action="store_true")

    args = parser.parse_args()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    info_handler = logging.FileHandler('lists2axon_converted.log')
    error_file_handler = logging.FileHandler('lists2axon_error.log')

    console_handler.setLevel(logging.INFO)
    info_handler.setLevel(logging.INFO)
    info_handler.addFilter(InfoFilter())
    error_file_handler.setLevel(logging.ERROR)

    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(log_format)
    info_handler.setFormatter(log_format)
    error_file_handler.setFormatter(log_format)

    logger.addHandler(console_handler)
    logger.addHandler(info_handler)
    logger.addHandler(error_file_handler)

    if args.all:
        all_lr_lists = get_all_lr7_lists(args.lr_api_key, args.lr_url, logger, exclude_types=exclude_lr_list_types)
        if all_lr_lists:
            for lr_list in all_lr_lists:
                axon_lists = create_axon_list_payload(lr_list['name'], args.lr_api_key, base_url=args.lr_url,
                                                      logger=logger, exclude_types=exclude_lr_list_types)
                if axon_lists:
                    if args.debug:
                        save_axon_list_to_file(axon_lists, 'C:\\LogRhythm\\AxonLists', lr_list['name'], logger)
                    create_axon_lists(axon_lists, args.axon_api_key, args.tenant_id, args.axon_url, logger=logger,
                                      debug=args.debug)
    elif args.search:
        log_message(logger, 'info', 'Searching for Axon Lists with the search term: {}'.format(args.search))
        log_message(logger, 'info', search_axon_list(args.search, args.axon_api_key, args.tenant_id, logger=logger,
                                                     debug=args.debug))
    else:
        axon_list = create_axon_list_payload(args.name, args.lr_api_key, base_url=args.lr_url, logger=logger,
                                             exclude_types=exclude_lr_list_types)
        if axon_list:
            if args.debug:
                save_axon_list_to_file(axon_list, 'C:\\LogRhythm\\AxonLists', args.name, logger)
            create_axon_lists(axon_list, args.axon_api_key, args.tenant_id, args.axon_url, logger=logger, debug=args.debug)


if __name__ == '__main__':
    list_cli()
