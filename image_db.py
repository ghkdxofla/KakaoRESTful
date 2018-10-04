'''
Date : 2018-09-28

Author: Hwang Taelim

Content: DB for famous paintings
'''
from pymongo import MongoClient


class DBConnect(object):
    def __init__(self, host="127.0.0.1", port=27017, db="admin"):
        print("--INIT MONGODB CONNECTION--")
        self.client = MongoClient(host=host, port=port)
        self.db = self.client.get_database(db)
        self.collection = self.db['collection']
        print("--CLIENT : {0}--".format(self.client))
        print("--DB : {0}--".format(self.db))
        print("--COLLECTION : {0}--".format(self.collection))

    def set_db(self, db):
        self.db = self.client.get_database(db)
        return

    def set_collection(self, collection="collection"):
        self.collection = self.db[collection]
        return

    def set_item(self, item):
        if not item:
            return
        try:
            result = self.collection.update_one(
                {
                    "name": item["name"]
                },
                {
                    "name": item["name"],
                    "attribute": item["attribute"]
                },
                upsert=True,
            )
            return result
        except Exception as e:
            print(e)

    def get_item(self, name):
        result = self.collection.find(
            {
                "name": name
            }
        )
        return list(result)