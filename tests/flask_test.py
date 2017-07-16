import unittest, json
from src.server import app

class FlaskTestCase(unittest.TestCase):

    # Тесты, проверяющие корректность обработки запросов сервером

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_response_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_response_data(self):
        result = self.app.get('/')
        self.assertEqual(result.data, b'Simple telegram events notifier')

    def test_fire_event_wrong_header(self):
        result = self.app.post('/fire', data=dict(
            message="Test"
        ))
        self.assertEqual(result.status_code, 400)

    def test_fire_event_correct_header_wrong_data(self):
        result = self.app.post('/fire', data=json.dumps(dict(
            test="Test"
        )), content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_fire_event_correct_header_correct_data(self):
        result = self.app.post('/fire', data=json.dumps(dict(
            message="Test"
        )), content_type='application/json')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()