"""
Тестовый модуль для code.py
"""
import unittest
import code


class TestCode(unittest.TestCase):
    def test_add(self):
        """
        Тест юнита add()
        """
        self.assertEqual(code.add(1, 1), 2)  # Тестовый случай
        self.assertEqual(code.add(0, 0), 0)
        self.assertEqual(code.add(-10, 10), 0)
        self.assertEqual(code.add(4, 5), 9)
        self.assertEqual(code.add(-2, -7), -9)

    def test_sub(self):
        """
        Тест юнита sub()
        """
        self.assertEqual(code.sub(1, 1), 0)  # Тестовый случай
        self.assertEqual(code.sub(10, 2), 8)
        self.assertEqual(code.sub(-10, 10), -20)
        self.assertEqual(code.sub(10, -3), 13)
        self.assertEqual(code.sub(-24, 0), -24)

    def test_mult(self):
        """
        Тест юнита mult()
        """
        self.assertEqual(code.mult(2, 2), 4)
        self.assertEqual(code.mult(0, 2), 0)
        self.assertEqual(code.mult(10, 10), 100)
        self.assertEqual(code.mult(-2, -2), 4)
        self.assertEqual(code.mult(3, -4), -12)


if __name__ == "__main__":
    unittest.main()
