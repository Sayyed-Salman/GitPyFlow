import unittest
from app import create_app


app = create_app()


class TestAddFunction(unittest.TestCase):

    def test_addition(self):
        with app.test_client() as client:
            response = client.get('/add/4/5')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), '4 + 5 = 9')

    def test_missing_variable(self):
        with app.test_client() as client:
            response = client.get('/add/4/')
            self.assertEqual(response.status_code, 404)

    def test_invalid_variable(self):
        with app.test_client() as client:
            response = client.get('/add/4/foo')
            self.assertEqual(response.status_code, 404)
