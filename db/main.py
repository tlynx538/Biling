from pymongo import MongoClient
class MongoDBClient: 
    conn = None 
    def __init__(self):
        print("Initialising Connection to MongoDB")
        CONNECTION_STRING = "mongodb://localhost:27017/"
        self.conn = MongoClient(CONNECTION_STRING)
        self.db = self.conn['bill-db']
     
    def insertBill(self, bill):
        print(bill)
        self.db['bills'].insert_one(bill)

    def showBill(self, bill_id):    
        bills_collection = self.client['bills']
        pass 

