"""
retrieve class test
"""

from app import retrieve

def test_retrieve_init():
    """ Test the init of the retrieve class"""
    test_retrieve = retrieve.Retrieve()
    assert test_retrieve.config['test']['dev'] == "https://google.com"

def test_retrieve_method(mock_function, test_data):
    """tests api get function w mock test data"""
    mock_function.return_value = test_data
    test_retrieve = retrieve.Retrieve()
    assert test_retrieve.get_data() == {"id":1,"userId":1}
