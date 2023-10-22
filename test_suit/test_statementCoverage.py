import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class StatementCoverageTest(unittest.TestCase):
    def test1(self):
        actual = Triangle.classify(-8, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test2(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test3(self):
        actual = Triangle.classify(8, 9, 10)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test4(self):
        actual = Triangle.classify(1, 7, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test5(self):
        actual = Triangle.classify(5, 5, 8)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test6(self):
        actual = Triangle.classify(5, 8, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test7(self):
        actual = Triangle.classify(8, 5, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test8(self):
        actual = Triangle.classify(11, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test9(self):
        actual = Triangle.classify(10, -8, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test10(self):
        actual = Triangle.classify(10, 10, -8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test11(self):
        actual = Triangle.classify(2, 10, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test12(self):
        actual = Triangle.classify(10, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
