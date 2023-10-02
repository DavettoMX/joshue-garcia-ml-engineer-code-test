import unittest

from app import api
from flask import Flask


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = Flask(__name__)
        self.app.register_blueprint(api)  # Register your Blueprint with the test app
        self.client = self.app.test_client()

    def test_ner_api_endpoint(self):
        # Define a sample payload
        payload = {
            "oraciones": [
                "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                "San Francisco considera prohibir los robots de entrega en la acera."
                # Add more sentences here if you want to test the API with more sentences
            ]
        }

        # Define the expected response
        expected_response = {
            "resultado": [
                {
                    "entidades": {
                        "Apple": "ORG",
                        "Reino Unido": "LOC"
                    },
                    "oración": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares."
                },
                {
                    "entidades": {
                        "San Francisco": "LOC"
                    },
                    "oración": "San Francisco considera prohibir los robots de entrega en la acera."
                }
            ]
        }

        # Send a POST request to the /api/v1/ner endpoint
        response = self.client.post('/api/v1/ner', json=payload)

        # Parse the response JSON
        data = response.get_json()

        # Assert the response data
        self.assertEqual(data, expected_response)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
