import unittest
from isTriangle import Triangle

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


if __name__ == '__main':
    unittest.main()
