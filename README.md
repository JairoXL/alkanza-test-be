## 1. Install requirements:

`pip install -r requirements.txt`

## 2. Running app:

First, build database (SQLite):

`python alkanza/models.py`

### Windows:

`waitress-serve --port=8000 alkanza.app:api`

### Mac/Linux:

TODO

## 3. API endpoints

- [GET] `/history`
    
    Lists all records
    
- [POST] `/history`

    Saves a new record
    
    **Body Sample:**
    
    ```
    {
        "username": "SomeUser",
        "radius": 250,
        "ref_location": {
            "latitude": "4.7250648",
            "longitude": "-74.2325567"
        },
        "medical_centers": {
            "data": [
                {
                    "latitude": "4.714458",
                    "longitude": "-74.2183517"
                }
            ]
        }
    }
    ```

