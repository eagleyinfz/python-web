import unittest
from src.app import app

class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_main_page(self):
        page = self.app.get("/")
        assert page.status_code == 200
        assert 'Hello' in str(page.data)

if __name__ == '__main__':
    unittest.main()