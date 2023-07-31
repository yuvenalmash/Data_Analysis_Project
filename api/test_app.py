import unittest
import requests

class TestApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000/predict_gdp_per_capita'

    def test_predict_gdp_per_capita(self):
        input_data = {
            'continent': 'Europe',
            'population': 1000000,
            'gross_national_savings': 0.2,
            'features': [0.1, 0.2, 0.3, 0.4, 0.5]
        }

        response = requests.post(self.base_url, json=input_data)

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check if the response contains the predicted GDP per capita
        self.assertIn('predicted_gdp_per_capita', response.json())

        # Check if the predicted GDP per capita is a number
        self.assertIsInstance(response.json()['predicted_gdp_per_capita'], float)

    def test_missing_parameter(self):
        input_data = {
            'continent': 'Europe',
            'population': 1000000,
            'gross_national_savings': 0.2,
        }

        response = requests.post(self.base_url, json=input_data)

        # Check if the request was unsuccessful (status code 400)
        self.assertEqual(response.status_code, 400)

        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check if the response contains an error message
        self.assertIn('error', response.json())

    def test_unexpected_parameter(self):
        input_data = {
            'continent': 'Europe',
            'population': 1000000,
            'gross_national_savings': 0.2,
            'features': [0.1, 0.2, 0.3, 0.4, 0.5],
            'unexpected_parameter': 'unexpected_value'
        }

        response = requests.post(self.base_url, json=input_data)

        # Check if the request was unsuccessful (status code 400)
        self.assertEqual(response.status_code, 400)

        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check if the response contains an error message
        self.assertIn('error', response.json())

    def test_unexpected_http_method(self):
        response = requests.get(self.base_url)

        # Check if the request was unsuccessful (status code 405)
        self.assertEqual(response.status_code, 405)

        # Check if the response is in JSON format
        self.assertEqual(response.headers['Content-Type'], 'application/json')

        # Check if the response contains an error message
        self.assertIn('error', response.json())

if __name__ == '__main__':
    unittest.main()
