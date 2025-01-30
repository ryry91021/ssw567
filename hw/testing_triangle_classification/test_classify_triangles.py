import unittest
from classify_triangles import classify_triangle

class testTriangle(unittest.TestCase):
    def test_isEquilateral(self):
        self.assertEqual(classify_triangle(500,500,500), "equilateral")
    def test_isIsosceles(self):
        self.assertEqual(classify_triangle(6,6,8), "isosceles")
    def test_isScalene(self):
        self.assertEqual(classify_triangle(15,34,32), "scalene")
    def test_isRight(self):
        self.assertEqual(classify_triangle(3,4,5), "right")
    
    def test_negativeLengthError(self):
        with self.assertRaises(ValueError) as e:
            classify_triangle(-1, 2, 5)
    def test_improperTriangle(self):
        with self.assertRaises(ValueError) as e:
            classify_triangle(1000, 1, 1)


if __name__ == '__main__': unittest.main()