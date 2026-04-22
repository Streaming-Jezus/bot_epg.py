import json
import logging
from datetime import datetime


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_info(message):
    logging.info(message)


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        log_info(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        log_info(f"Error decoding JSON from the file: {file_path}")
        return None


def write_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            log_info(f"Successfully wrote to JSON file: {file_path}")
    except Exception as e:
        log_info(f"Error writing JSON to the file: {file_path}, Error: {str(e)}")


def format_timestamp(timestamp=None):
    if timestamp is None:
        timestamp = datetime.utcnow()
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')
