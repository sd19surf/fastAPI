"""
retrieve class test
"""

from unittest.mock import Mock, patch
from app import retrieve

def test_retrieve_init():
    """ Test the init of the retrieve class"""
    test_retrieve = retrieve.Retrieve()
    assert test_retrieve.config['test']['dev'] == "https://google.com"

