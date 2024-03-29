# Simple Billing API

## API for creating, deleting and viewing bills.

[DEPRECATED]
~

### Stack Used:

1. MongoDB Database/pymongo.
2. FastAPI

### Installation and Setup:

1. Install using `pip install -r requirements.txt` to install packages.
2. Make sure MongoDB is installed and running correctly.
3. Once installed, run using `uvicorn main:app --reload`
4. Use Postman to work with the routes.

~

### Features:

1. Creates Bill by using '/bill/create' route.
2. Shows Bill by bill id using '/bill/find/'.
3. Delete Bill by bill id using '/bill/delete/'.

### TODO:

1. Auth (possibly using Passport or something equivalent)
2. Integration for other services.

### Notes:

1. There will be no update logic, because a new bill needs to be created and the one that is slated to be updated shall be deleted. (By Design)
2. Update 03/29/2024: Porting Python API to Go API for full support in implementing coroutines and possibly for following non sequential, non-locking operations.
