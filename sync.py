import json
from datetime import datetime, timedelta
from dms_utils import get_files

def generate_sync_operations(start_date, end_date):
  # temp stores for files and operations
  previous_files = {}
  total_operations = {}

  # adjust end date bc daterange is upper bound exclusive
  end += timedelta(days=1)
  
  # get list of files from start_date to end_date:
  for date in daterange(start, end):
    files = get_files(date.strftime('%Y-%m-%d'))
    current_files = {}
    operations_today = []

    for f in files:
      # instantiate prev_files on first date so existing files don't count as created
      if not previous_files:
        previous_files[f['id']] = {'id': f['id'], 'name': f['name'], 'meta': f['meta']}
      current_files[f['id']] = {'id': f['id'], 'name': f['name'], 'meta': f['meta']}

    # call helpers to determine which operations occurred today
    operations_today += list_created_files(previous_files, current_files)
    operations_today += list_deleted_files(previous_files, current_files)
    operations_today += list_updated_filenames(previous_files, current_files)
    operations_today += list_updated_filemetas(previous_files, current_files)

    # add operations to response after start_date
    if date > start:
      total_operations[date.strftime('%Y-%m-%d')] = operations_today

    # update prev_files
    previous_files = current_files

  return total_operations

def list_created_files(prev, curr):
  ops = []
  for file_id in curr.keys():
    if file_id not in prev:
      ops.append({'createFile': curr[file_id]})
  return ops

def list_deleted_files(prev, curr):
  ops = []
  for file_id in prev.keys():
    if file_id not in curr:
      ops.append({'deleteFile': {'id': prev[file_id]['id']}})
  return ops

def list_updated_filenames(prev, curr):
  ops = []
  for file_id in curr.keys():
    if file_id in prev and prev[file_id]['name'] != curr[file_id]['name']:
      ops.append({'updateFileName': {'id': curr[file_id]['id'], 'name': curr[file_id]['name']}})
  return ops

def list_updated_filemetas(prev, curr):
  ops = []
  for file_id in curr.keys():
    if file_id in prev and prev[file_id]['meta'] != curr[file_id]['meta']:
      ops.append({'updateFileMeta': {'id': curr[file_id]['id'], 'meta': curr[file_id]['meta']}})
  return ops

def daterange(start, end):
  for n in range(int((end - start).days)):
    yield start + timedelta(n)

def string_to_date(date):
  return datetime.strptime(date, '%Y-%m-%d')