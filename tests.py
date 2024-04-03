import unittest
from unittest.mock import Mock, patch
from sync import (
  generate_sync_operations,
  list_created_files,
  list_deleted_files,
  list_updated_filenames,
  list_updated_filemetas
)

class TestSync(unittest.TestCase):
  def test_list_created_files(self):
    prev = {
      'test-file-id-1': {
        'id': 'test-file-id-1',
        'name': 'test-name-1',
        'meta': {}
      }
    }
    curr = {
      'test-file-id-1': {
        'id': 'test-file-id-1',
        'name': 'test-name-1',
        'meta': {}
      },
      'test-file-id-2': {
        'id': 'test-file-id-2',
        'name': 'test-name-2',
        'meta': {}
      }
    }
    ops = list_created_files(prev, curr)
    res = [{
      'createFile': {
        'id': 'test-file-id-2',
        'name': 'test-name-2',
        'meta': {}
      }
    }]
    self.assertTrue(res == ops)

  def test_list_deleted_files(self):
      prev = {
      'test-file-id-1': {
        'id': 'test-file-id-1',
        'name': 'test-name-1',
        'meta': {}
      },
      'test-file-id-2': {
        'id': 'test-file-id-2',
        'name': 'test-name-2',
        'meta': {}
      }
    }
      curr = {
        'test-file-id-1': {
          'id': 'test-file-id-1',
          'name': 'test-name-1',
          'meta': {}
        }
      }
      ops = list_deleted_files(prev, curr)
      res = [{
        'deleteFile': {
          'id': 'test-file-id-2'
        }
      }]
      self.assertTrue(res == ops)

  def test_list_updated_filenames(self):
      prev = {
      'test-file-id-1': {
        'id': 'test-file-id-1',
        'name': 'test-name-1',
        'meta': {}
      }
    }
      curr = {
        'test-file-id-1': {
          'id': 'test-file-id-1',
          'name': 'test-name-2',
          'meta': {}
        }
      }
      ops = list_updated_filenames(prev, curr)
      res = [{
        'updateFileName': {
          'id': 'test-file-id-1',
          'name': 'test-name-2'
        }
      }]
      self.assertTrue(res == ops)

  def test_list_updated_filemetas(self):
      prev = {
      'test-file-id-1': {
        'id': 'test-file-id-1',
        'name': 'test-name-1',
        'meta': {}
        }
      }
      curr = {
        'test-file-id-1': {
          'id': 'test-file-id-1',
          'name': 'test-name-1',
          'meta': {'cat': 'old'}
        }
      }
      ops = list_updated_filemetas(prev, curr)
      res = [{
        'updateFileMeta': {
          'id': 'test-file-id-1',
          'meta': {'cat': 'old'}
        }
      }]
      self.assertTrue(res == ops)

if __name__ == '__main__':
  unittest.main()