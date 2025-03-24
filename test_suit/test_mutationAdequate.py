import unittest
from isTriangle import Triangle

class TestMutationAdequate(unittest.TestCase):

    def test_invalid_triangles(self):
        self.assertEqual(Triangle.classify(0, 1, 2), Triangle.Type.INVALID)  
        self.assertEqual(Triangle.classify(-1, 5, 6), Triangle.Type.INVALID) 
        self.assertEqual(Triangle.classify(1, 2, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(10, 1, 1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1, 1, 3), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(1000, 1, 1), Triangle.Type.INVALID)

    def test_scalene_triangles(self):
        self.assertEqual(Triangle.classify(3, 4, 5), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(7, 8, 9), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(2, 3, 4), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(999, 1000, 1001), Triangle.Type.SCALENE)

    def test_isosceles_triangles(self):
        self.assertEqual(Triangle.classify(5, 5, 8), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(6, 8, 6), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(8, 6, 6), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(10, 10, 15), Triangle.Type.ISOSCELES)

    def test_equilateral_triangles(self):
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)
        self.assertEqual(Triangle.classify(100, 100, 100), Triangle.Type.EQUILATERAL)

if __name__ == '__main__':
   unittest.main()