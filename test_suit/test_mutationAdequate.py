import unittest
from isTriangle import Triangle

"""
class TestTriangle(unittest.TestCase):

    def test_invalid_triangle(self):
        self.assertEqual(Triangle.classify(0, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 0, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, -1, 2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(10, 10, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 10, 10), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(10, 0, 10), Triangle.Type.INVALID)

    def test_scalene_triangle(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(7, 24, 25), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(8, 15, 17), Triangle.Type.SCALENE)

    def test_equilateral_triangle(self):
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(10, 10, 10), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, -1, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 2, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 4, 2), Triangle.Type.INVALID)
        #self.assertEqual(Triangle.classify(5, 6, 2), Triangle.Type.SCALENE)


    def test_isosceles_triangle(self):
        self.assertEqual(Triangle.classify(3, 3, 4), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 6, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 4, 4), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 5, 7), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(3,3,6), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(3,6,3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(6,3,3), Triangle.Type.INVALID)

"""

class TestTriangle(unittest.TestCase):

    def test_01(self):
        actual = Triangle.classify(0, 1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_02(self):
        actual = Triangle.classify(1, 0, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_03(self):
        actual = Triangle.classify(1, 2, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_04(self):
        actual = Triangle.classify(-1, 1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_05(self):
        actual = Triangle.classify(1, -1, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_06(self):
        actual = Triangle.classify(1, 2, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_07(self):
        actual = Triangle.classify(10, 10, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_08(self):
        actual = Triangle.classify(0, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_09(self):
        actual = Triangle.classify(10, 0, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_10(self):
        actual = Triangle.classify(3, 4, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_11(self):
        actual = Triangle.classify(7, 24, 25)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_12(self):
        actual = Triangle.classify(8, 15, 17)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_13(self):
        actual = Triangle.classify(5, 5, 5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_14(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_15(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_16(self):
        actual = Triangle.classify(-1, -1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_17(self):
        actual = Triangle.classify(0, 1, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_18(self):
        actual = Triangle.classify(1, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_19(self):
        actual = Triangle.classify(2, 4, 2)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_20(self):
        actual = Triangle.classify(5, 5, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_21(self):
        actual = Triangle.classify(3, 3, 4)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_22(self):
        actual = Triangle.classify(5, 6, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_23(self):
        actual = Triangle.classify(2, 2, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_24(self):
        actual = Triangle.classify(3, 3, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_25(self):
        actual = Triangle.classify(3, 6, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_26(self):
        actual = Triangle.classify(6, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_27(self):
        actual = Triangle.classify(5, 4, 4)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual,expected)

if __name__ == '__main':
    unittest.main()

