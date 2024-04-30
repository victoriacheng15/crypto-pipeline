import os, psycopg2, logging
from utils.mongo import MongoDB
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("MONGO_DB")
COL_NAME = os.environ.get("MONGO_COLLECTION")

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")


class DataMigration:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.conn = psycopg2.connect(
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            database=POSTGRES_DB,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
        )
        self.cursor = self.conn.cursor()

    def connect(self):
        try:
            self.logger.info("Connecting to PostgreSQL...")
            return self.conn
        except Exception as e:
            self.logger.error(f"Failed to connect to PostgreSQL: {e}")
            return None

    def close(self):
        try:
            if self.conn:
                self.cursor.close()
                self.conn.close()
                self.logger.info("PostgreSQL connection closed.")
        except Exception as e:
            self.logger.error(f"Failed to close PostgreSQL connection: {e}")

    def migrate(self):
        mongo = MongoDB()
        try:
            mongo.connect()
            items = mongo.get_all_documents(COL_NAME)
            query = """
        INSERT INTO raw_data (name, symbol, current_price, market_cap, total_supply, high_24h, low_24h, ath, ath_date, atl, atl_date, last_updated, save_timestamp) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
      """

            for data in items:
                self.cursor.execute(
                    query,
                    (
                        data["name"],
                        data["symbol"],
                        data["current_price"],
                        data["market_cap"],
                        data["total_supply"],
                        data["high_24h"],
                        data["low_24h"],
                        data["ath"],
                        data["ath_date"],
                        data["atl"],
                        data["atl_date"],
                        data["last_updated"],
                        data["save_timestamp"],
                    ),
                )
                self.conn.commit()

        except Exception as e:
            logging.info(f"Error during data migration: {e}")
        finally:
            mongo.close()
