import unittest
import calculator

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
