import logging, os
from sys import argv
from utils.mongo import MongoDB
from utils.data_migration import DataMigration
from utils.extraction import get_coin_data, to_dict

COL_NAME = os.environ.get("MONGO_COLLECTION")


def insert_data(mongo):
    if not mongo.connect():
        return

    items = get_coin_data(2)
    for item in items:
        crypto = to_dict(item)
        mongo.insert_one(COL_NAME, crypto)
    count = mongo.get_counts(COL_NAME)
    logging.info(f"The current data count in the collection: {count}")
    mongo.close()


def delete_data(mongo):
    if not mongo.connect():
        return

    mongo.delete_all(COL_NAME)
    mongo.close()


def main(action):
    logging.basicConfig(level=logging.INFO)
    mongo = MongoDB()
    migration = DataMigration()
    if action == "data":
        insert_data(mongo)
    elif action == "delete":
        delete_data(mongo)
    elif action == "migration":
        migration.connect()
        migration.migrate()
    else:
        logging.error(f"Invalid action: {action}. Please enter 'data' or 'delete'.")


if __name__ == "__main__":
    action = argv[1]
    main(action)
