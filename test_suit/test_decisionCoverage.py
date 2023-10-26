import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class DecisionCoverageTest(unittest.TestCase):
    def test1(self): # line 39: true 51%
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test2(self): # line 21: true 55%
        actual = Triangle.classify(-1, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test3(self): # line 26: true 67%
        actual = Triangle.classify(8, 8, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test4(self): # line 28: true 76%
        actual = Triangle.classify(8, 10, 8)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test5(self): # line 30: true 84%
        actual = Triangle.classify(10, 8, 8)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test6(self): # line 34: true 92%
        actual = Triangle.classify(8, 1, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test7(self): # line 36: true 96%
        actual = Triangle.classify(8, 5, 4)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
    
    def test8(self): # line 46 false: 100%
        actual = Triangle.classify(8, 8, 20)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
