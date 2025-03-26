import unittest
from src.main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Mai Therapy Agent", response.data)

    def test_chat_endpoint(self):
        response = self.app.post("/chat", json={"message": "Hello", "lang": "en"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json)

if __name__ == "__main__":
    unittest.main()
