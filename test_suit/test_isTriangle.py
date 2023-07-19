import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
