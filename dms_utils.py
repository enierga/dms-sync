import os.path
import json
import requests

def read_jsonl(date):
  responses_dir = './dms-responses/'
  filepath = responses_dir + f"{date}.jsonl"

  try:
    with open(filepath, 'r') as file:
      contents = []
      for row in file:
        contents.append(json.loads(row))
      return contents
  except:
    return "File not found"

# for calling mock dms endpoint to get files for a particular date
def get_files(date):
  res = requests.get('http://127.0.0.1:8001/files', params={'date':date})
  file_dict = json.loads(res.content)
  return file_dict['files']