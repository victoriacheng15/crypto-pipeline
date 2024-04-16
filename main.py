from sys import argv
from utils.db_operations import MongoDB
from utils.extraction import get_coin_data, to_dict


def main(action):
    if action == "data":
        items = get_coin_data(2)
        for item in items:
            crypto = to_dict(item)
            mongo.insert_one("data", crypto)
        count = mongo.get_counts("data")
        print(f"current data count: {count}")
    elif action == "delete":
        mongo.delete_all("data")
    else:
        print("Invalid action. Please enter 'data' or 'delete'.")


if __name__ == "__main__":
    mongo = MongoDB("crypto")
    action = argv[1]
    print(action)
    if mongo.connect():
        print("\nstarting the process...\n")
        main(action)
        print("\nthe process is complete...\n")
