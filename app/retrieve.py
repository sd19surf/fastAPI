"""
grab some data functions
"""


import urllib3


class Retrieve():

    def __init__(self):
        """initialize with something"""
        self.config = {"test":{"dev":"https://google.com"}}
        self.data = self.get_data()

    def get_data(self):
        """basic external api call method"""
        http = urllib3.PoolManager()
        url = 'http://dummy.restapiexample.com/api/v1/employee/1'
        resp = http.request('GET', url)    
        return resp.data.decode('utf-8')
