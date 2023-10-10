import unittest
import requests

class TestAPIExample(unittest.TestCase):
    def test_get_request(self):
        api_url = "https://www.python.org"
        response = requests.get(api_url)
        
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the text "Welcome to Python.org"
        self.assertIn("Welcome to Python.org", response.text)

if __name__ == '__main__':
    unittest.main()
