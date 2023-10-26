import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class StatementCoverageTest(unittest.TestCase):
    def test1(self): # line 22
        actual = Triangle.classify(-8, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test2(self): # line 40 equilateral 68%
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test3(self): # line 36/37 scalene 74%
        actual = Triangle.classify(8, 9, 10)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test4(self): # line 34/35 invalid inequality 77%
        actual = Triangle.classify(1, 7, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test5(self): # line 42/43 a==b ISOSCELES 84%
        actual = Triangle.classify(5, 5, 8)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test6(self): # line 44/45 a==c ISOSCELES 90%
        actual = Triangle.classify(5, 8, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test7(self): # line 46/47 b==c ISOSCELES 97%
        actual = Triangle.classify(8, 5, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test8(self): # line 49 two sides equal, but invalid 
        actual = Triangle.classify(11, 5, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
