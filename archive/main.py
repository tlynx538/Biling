from fastapi import FastAPI
from db.main import MongoDBClient
from pydantic import BaseModel
from typing import Dict, List
import uuid 

app = FastAPI()
client = MongoDBClient()

class BillItems(BaseModel):
    sl_no : int 
    desc: str 
    qty: int 
    price: float  

class AddBill(BaseModel):
    items: Dict[str, List[BillItems]]
    total_price: float
    status_id: int 

@app.get('/')
def home():
    return {"Welcome to Billing API!"}

@app.post('/bill/create')
def create_bill(bill_: AddBill):
    # generate bill id 
    bill_id = str(uuid.uuid4())
    # validate bill 
    bill_items = []
    grand_total = 0
    for i in bill_.items['list_items']:
        grand_total += (i.price * i.qty) 
        item = {"sl_no": i.sl_no, "desc": i.desc, "qty": i.qty, "price": i.price}
        bill_items.append(item)

    # bill preparation
    bill = {"bill_id": bill_id, "items": bill_items, "total_price": bill_.total_price, "bill_status": bill_.status_id}
    if float(grand_total) == float(bill_.total_price):
    # insert bill to db
        res = client.insertBill(bill)
        if res is True:
            return {"message" : "Bill Successfully Created"}
        else:
            return {"message" : "An Error has occured", "error_message" : str(res[0])}

    else:
        return {"message": "Error in Validating Prices"}

@app.get('/bill/find/'+'{bill_id}')
def show_bill(bill_id):
    bill = client.showBill(bill_id)
    if bill is not None: 
        return bill 
    else:
        return {"message" : "No Bill Found"}

@app.get('/bill/delete/'+'{bill_id}')
def delete_bill(bill_id):
    res = client.deleteBill(bill_id)
    if res is True:
        return {"message" : "Bill "+str(bill_id)+" has been deleted."}
    else:
        return {"message" : "An Error has occured", "error_message" : str(res[0])}