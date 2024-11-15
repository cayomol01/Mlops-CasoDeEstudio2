import unittest
from model import prueba


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(prueba(2, 3), 6)
        self.assertEqual(prueba(-1, 1), -1)

if __name__ == "__main__":
    unittest.main()