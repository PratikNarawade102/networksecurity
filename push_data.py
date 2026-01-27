import os, sys, json
import certifi
import pandas as pd
import pymongo
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class NetworkDataExtract:

    def __init__(self):
        try:
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=certifi.where()
            )
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            return list(json.loads(data.T.to_json()).values())
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            db = self.mongo_client[database]
            col = db[collection]
            col.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = r"Network_Data\Phishing_Legitimate_full.csv"
    DATABASE = "NetworkSecurity"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(FILE_PATH)
    print(len(records))

    count = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(count)
