import unittest
from triangle import area
from triangle import perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zer0_mul(self):
        res = area(7,4)
        self.assertEqual(res, 14)

    def test_square_mul(self):
        res = area(10, 2)
        self.assertEqual(res, 10)

    def test_square_perimeter_zero(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_square_perimeter(self):
        res = perimeter(7, 1, 10)
        self.assertEqual(res, 18)

    def test_square_area_neg(self):
        res = area(-123, 0)
        self.assertEqual(res, "Change input parameters")

    def test_square_perimeter_neg(self):
        res = perimeter(-123, 0, 2)
        self.assertEqual(res, "Change input parameters")


if __name__ == '__main__':
    unittest.main()