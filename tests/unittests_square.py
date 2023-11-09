import unittest
from square import area
from square import perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zer0_mul(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_square_perimeter_zero(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_square_perimeter(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_square_area_neg(self):
        res = area(-123)
        self.assertEqual(res, "Change input parameters")

    def test_square_perimeter_neg(self):
        res = perimeter(-123)
        self.assertEqual(res, "Change input parameters")


if __name__ == '__main__':
    unittest.main()