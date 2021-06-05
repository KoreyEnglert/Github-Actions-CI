import unittest
import calculator


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 2), 4)

    def test_sub(self):
        self.assertEqual(calculator.sub(2, 2), 0)

    def test_mul(self):
        self.assertEqual(calculator.mul(2, 2), 4)

    def test_div(self):
        self.assertEqual(calculator.div(2, 2), 1)


if __name__ == '__main__':
    unittest.main()
