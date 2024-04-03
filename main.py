from fastapi import FastAPI, HTTPException
from datetime import datetime
from dms_utils import read_jsonl
from sync import generate_sync_operations

app = FastAPI()

@app.get("/operations")
def list_operations(start: str, end: str):
  # convert date args into datetime and check validity of range
  start_date = datetime.strptime(start, '%Y-%m-%d')
  end_date = datetime.strptime(end, '%Y-%m-%d')
  if end_date < start_date:
    raise HTTPException(status_code=400, detail='Invalid date range')

  return {
    "operations": generate_sync_operations(start_date, end_date)
  }

# helper endpoint to get sample dms responses
dms = FastAPI()
@dms.get("/files")
def list_files(date: str):
  return {
    "files": read_jsonl(date)
  }