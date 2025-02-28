import unittest
from classify_triangles import classify_triangle

class TestTriangle(unittest.TestCase):
    """Unit tests for classify_triangle function."""

    def test_isEquilateral(self):
        """Test for an equilateral triangle."""
        self.assertEqual(classify_triangle(500, 500, 500), "equilateral")

    def test_isIsosceles(self):
        """Test for an isosceles triangle."""
        self.assertEqual(classify_triangle(6, 6, 8), "isosceles")
        self.assertEqual(classify_triangle(8, 6, 6), "isosceles")
        self.assertEqual(classify_triangle(6, 8, 6), "isosceles")

    def test_isScalene(self):
        """Test for a scalene triangle."""
        self.assertEqual(classify_triangle(15, 34, 32), "scalene")
        self.assertEqual(classify_triangle(10, 20, 25), "scalene")

    def test_isRight(self):
        """Test for a right triangle."""
        self.assertEqual(classify_triangle(3, 4, 5), "right")
        self.assertEqual(classify_triangle(5, 12, 13), "right")
        self.assertEqual(classify_triangle(8, 15, 17), "right")
        self.assertEqual(classify_triangle(7, 24, 25), "right")

    def test_negativeLengthError(self):
        """Test that negative side lengths raise a ValueError."""
        with self.assertRaises(ValueError):
            classify_triangle(-1, 2, 5)
        with self.assertRaises(ValueError):
            classify_triangle(5, -2, 5)
        with self.assertRaises(ValueError):
            classify_triangle(3, 4, -5)

    def test_zeroLengthError(self):
        """Test that zero side lengths raise a ValueError."""
        with self.assertRaises(ValueError):
            classify_triangle(0, 5, 5)
        with self.assertRaises(ValueError):
            classify_triangle(5, 0, 5)
        with self.assertRaises(ValueError):
            classify_triangle(5, 5, 0)

    def test_improperTriangle(self):
        """Test for non-triangular cases where the sum of two sides is not greater than the third."""
        with self.assertRaises(ValueError):
            classify_triangle(1000, 1, 1)
        with self.assertRaises(ValueError):
            classify_triangle(10, 5, 5)
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, 3)

    def test_floatingPointValues(self):
        """Test that floating-point values are classified correctly."""
        self.assertEqual(classify_triangle(3.0, 4.0, 5.0), "right")
        self.assertEqual(classify_triangle(5.5, 5.5, 5.5), "equilateral")
        self.assertEqual(classify_triangle(7.1, 7.1, 10.0), "isosceles")
        self.assertEqual(classify_triangle(9.5, 10.5, 12.5), "scalene")

if __name__ == '__main__':
    unittest.main()
