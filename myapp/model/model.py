class KeyValue:
    def __init__(self, db):
        self.db = db

    def add(self, key, value):
        self.db.collection.insert_one({'_id': key, 'value': value})

    def get(self, key):
        return self.db.collection.find_one({'_id': key})

    def update(self, key, value):
        self.db.collection.update_one({'_id': key}, {"$set": {'value': value}})
    
    def get_all(self):
        cursor = self.collection.find({})
        results = []
        for doc in cursor:
            results.append({"key": doc["key"], "value": doc["value"]})
        return results
