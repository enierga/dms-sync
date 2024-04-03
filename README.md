## DMS Sync
An API with a single endpoint that produces the list of operations between two dates.

### Request and Response Formats
#### Request:
The endpoint `GET /operations` takes two parameters: `start_date` and `end_date`, as `YYYY-MM-DD` strings
#### Response
The response is returned as a map with dates as keys and a list of operations that occurred on that particular date as the value.
##### Sample Request and Response:
```
GET /operations?start=2023-01-01&end=2023-01-03

{
    "operations": {
        "2023-01-02": [
            {
                "createFile": {
                    "id": "ea390747-4741-48f2-a63e-101c120479f2",
                    "name": "depo-p",
                    "meta": {}
                }
            },
            {
                "updateFileName": {
                    "id": "d119188b-46d9-4c6d-bd82-133dbba133c3",
                    "name": "decision-1"
                }
            }
        ],
        "2023-01-03": [
            {
                "deleteFile": {
                    "id": "d119188b-46d9-4c6d-bd82-133dbba133c3"
                }
            },
        ...
```
Documentation about the API can also be found at `/docs`.
###### DMS Endpoint

To aid in development, a mock DMS endpoint was created to simulate an external service for retrieving files for a particular day. This is a simple `GET` request on a different port. The request takes in a single date to grab a corresponding `.jsonl` file in the folder `dms-responses`.

### Getting Started
In order to run everything, you will need FastAPI and uvicorn:<br/>
```
pip install fastapi
pip install "uvicorn[standard]"
```

To run the service:<br/>
```
python3 -m uvicorn main:app --reload
```
To run the mock DMS endpoint (and for development/testing):<br/>
```
python3 -m uvicorn main:dms --reload --port 8001
```

To run unit tests:
```
python3 -m unittest -v
```