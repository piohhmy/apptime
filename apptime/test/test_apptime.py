from flask import testing
import unittest
from apptime import apptime_api
import flask
import json


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.test_app = apptime_api.app.test_client()

    def test_get_usage_returns_json_resp(self):
        result = self.test_app.get('/apptime/user/Sam/apps/usage')
        self.assertEqual(result.status_code, 200)
        self.assertIn('usage', result.data)

    def test_post_usage_returns_ok(self):
        result = self.test_app.post('/apptime/user/Bobby/apps/usage',
                                    data=json.dumps({'name':'Angry Birds', 'usage': 10}),
                                    content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_post_device_returns_ok(self):
        result = self.test_app.post('/apptime/device',
                                    data=json.dumps({'name': 'Sally'}),
                                    content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_get_user_devices_returns_ok(self):
        result = self.test_app.get('/apptime/user/Tommy/devices')
        self.assertEqual(result.status_code, 200)
        self.assertIn('devices', result.data)

    def test_get_users(self):
        result = self.test_app.get('/apptime/users')
        self.assertEqual(result.status_code, 200)
        self.assertIn('users', result.data)
if __name__ == '__main__':
    unittest.main()