import unittest
from app_sort import app
import json

req = [10, 55, 6, 2, 14, 1]

class TestJsonNumbers(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.list_of_algorithms = ['bubble', 'tim', 'heap']
        self.base_url = '/'

    def test_bubble(self):
        response = self.app.post(self.base_url + self.list_of_algorithms[0] + '/', json=req)
        self.assertEqual(response.status_code, 200)
        sorted_req = sorted(req)
        self.assertEqual(json.loads(response.data), sorted_req)

    def test_tim(self):
        response = self.app.post(self.base_url + self.list_of_algorithms[1] + '/', json=req)
        self.assertEqual(response.status_code, 200)
        sorted_req = sorted(req)
        self.assertEqual(json.loads(response.data), sorted_req)

    def test_heap(self):
        response = self.app.post(self.base_url + self.list_of_algorithms[2] + '/', json=req)
        self.assertEqual(response.status_code, 200)
        sorted_req = sorted(req)
        self.assertEqual(json.loads(response.data), sorted_req)

if __name__ == "__main__":
    unittest.main()