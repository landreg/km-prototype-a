import unittest
from application import app

class TestService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_server_code(self):
        self.assertEqual((self.app.get('/')).status, '200 OK')
