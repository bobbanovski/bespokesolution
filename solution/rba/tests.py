from application import create_app as create_app_base
import unittest
from flask import session

class RbaApiTest(unittest.TestCase):
    def create_app(self):
        return create_app_base(
            TESTING = True,
            WTF_CSRF_ENABLED = False,
            )
        
    def setUp(self):
        self.app_factory = self.create_app()
        self.app = self.app_factory.test_client() # allows test module to handle requests
    
    #test that api is returning data, no 404s    
    def test_api(self):
        rv = self.app.get('/rba', follow_redirects=True)
        assert rv.status_code == 200