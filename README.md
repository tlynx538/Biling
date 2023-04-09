# Simple Billing API
## API for creating, updating and viewing bills.

### Stack Used:
1. MongoDB Database/pymongo.
2. FastAPI

### Features:
1. Creates Bill by using '/bill/create' route.
2. Shows Bill by bill id using '/bill/find/'.

### Installation and Setup:
1. Install using `pip install -r requirements.txt` to install packages.
2. Make sure MongoDB is installed and running correctly. 
3. Once installed, run using `uvicorn main:app --reload`
4. Use Postman to work with the routes.

### TODO:
1. Auth (possibly using Passport or something equivalent)
2. Logic for Updating Bills
3. Integration for other services.
