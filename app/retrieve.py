"""
grab some data functions
"""
import json
from urllib.request import urlopen


class Retrieve():
    """class to pull data from external resources"""

    def __init__(self):
        """initialize with something"""
        self.config = {"test":{"dev":"https://google.com"}}

    def get_data(self):
        """basic external api call method"""
        url = "https://api.github.com"
        with (urlopen(url)) as response:
            data_json = json.loads(response.read())
        return data_json
