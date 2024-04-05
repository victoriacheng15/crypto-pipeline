import datetime
from utils.db_operations import MongoDB
from utils.extraction import get_data


def main():
  items = get_data()
  for item in items:
    title = item.find("h2").get_text().strip()
    name, code = title.rsplit(maxsplit=1)
    price = item.find(class_="typography__StyledTypography-sc-owin6q-0 lnOdBs").get_text()[1:].replace(",","")
    extracted_date = datetime.datetime.now(tz=datetime.timezone.utc)
    crypto = {
      "name": name,
      "code": code,
      "price": price,
      "date": extracted_date
    }
    mongo.insert_one("data", crypto)
  count = mongo.get_counts("data")
  print(f"{count} items inserted")
  print(f"Items length: {len(items)}")

if __name__ == "__main__":
  mongo = MongoDB("crypto")

  if mongo.connect():
    print("\nstarting the process...\n")
    main()
    # mongo.delete_all("data")
    print("\nthe process is complete...\n")