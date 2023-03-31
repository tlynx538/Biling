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
    return {"message": "Success"}

@app.post('/create/bill')
def create_bill(bill_: AddBill):

    # generate bill id 
    bill_id = str(uuid.uuid4())
    # validate bill 
    bill_items = []
    grand_total = 0
    for i in bill_.items['list_items']:
        grand_total += i.price 
        item = {"sl_no": i.sl_no, "desc": i.desc, "qty": i.qty, "price": i.price}
        bill_items.append(item)

    # bill preparation
    bill = {"bill_id": bill_id, "items": bill_items, "total_price": bill_.total_price, "bill_status": bill_.status_id}
    if grand_total == bill_.total_price:
    # insert bill to db
        try:
            client.insertBill(bill)
            return {"message": "Bill Successfully Created for "+ bill_id}
        except Exception as e:
            return {"message": "Database Error has occured", "Error Message": str(e)}
    else:
        return {"message": "Error in Validating Prices"}