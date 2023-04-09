from pymongo import MongoClient
class MongoDBClient: 
    conn = None 
    def __init__(self):
        print("Initialising Connection to MongoDB")
        CONNECTION_STRING = "mongodb://localhost:27017/"
        self.conn = MongoClient(CONNECTION_STRING)
        self.db = self.conn['bill-db']
     
    def insertBill(self, bill):
        try:
            self.db['bills'].insert_one(bill)
            return True
        except Exception as e:
            return [e, False] 


    def showBill(self, bill_id):    
        bill_details = self.db['bills'].find_one({"bill_id": bill_id}, {'_id': False})
        return bill_details
    
    def deleteBill(self, bill_id):
        try:
            bill_details = self.db['bills'].delete_one({"bill_id": bill_id})
            return True 
        except Exception as e:
            return [e, False]
    
    def updateBill(self, bill_id, bill):
        pass
        

