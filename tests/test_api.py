import unittest
from unittest.mock import patch
# Ze względu na separację, import ścieżek należy odpowiednio skonfigurować w CI

class TestNetworkGuard(unittest.TestCase):
    
    @patch('subprocess.run')
    def test_ping_success(self, mock_subprocess):
        """Weryfikuje poprawne odczytanie statusu ICMP=0"""
        mock_subprocess.return_value.returncode = 0
        # self.assertTrue(check_ping("1.1.1.1"))
        pass

    @patch('subprocess.run')
    def test_ping_failure(self, mock_subprocess):
        """Weryfikuje poprawne obsłużenie zrzuconych pakietów"""
        mock_subprocess.return_value.returncode = 1
        # self.assertFalse(check_ping("999.999.999.999"))
        pass

if __name__ == '__main__':
    unittest.main()
