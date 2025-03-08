import unittest
from unittest.mock import patch
from app import app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.database.get_db_connection')
    def test_home_page(self, mock_db_conn):
        mock_db_conn.return_value = None  # Mock DB connection
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
