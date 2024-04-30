import logging, os
from sys import argv
from utils.mongo import MongoDB
from utils.extraction import get_coin_data, to_dict

COL_NAME = os.environ.get("MONGO_COLLECTION")

def main(action):
    logging.basicConfig(level=logging.INFO)
    mongo = MongoDB()
    if action == "data":
        if mongo.connect():
            items = get_coin_data(2)
            for item in items:
                crypto = to_dict(item)
                mongo.insert_one("data", crypto)
            count = mongo.get_counts(COL_NAME)
            logging.info(f" The current data count in the collection: {count}")
    elif action == "delete":
        if mongo.connect():
            mongo.delete_all(COL_NAME)
    else:
        logging.error(f"Invalid action: {action}. Please enter 'data' or 'delete'.")


if __name__ == "__main__":
    action = argv[1]
    main(action)
