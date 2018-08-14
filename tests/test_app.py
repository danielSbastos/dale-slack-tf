import json
import unittest

from app import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    def test_home_status_code(self):
        result = self.app.post("/dale_gif")

        response_data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertRegexpMatches(
            response_data["attachments"][0]["image_url"],
            r"https://media.giphy.com/media/.*/giphy.gif"
        )
        self.assertEqual(response_data["attachments"][0]["title"], "Vamo dale")
        self.assertEqual(response_data["response_type"], "in_channel")
