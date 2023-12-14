import unittest
from circle.py import area
from circle.py import perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zer0_mul(self):
        res = area(7)
        self.assertEqual(res, 153.93804002589985)

    def test_circle_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_circ_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)

    def test_circ_perimeter(self):
        res = perimeter(7)
        self.assertEqual(res, 43.982297150257104)

    def test_circ_area_neg(self):
        res = area(-123)
        self.assertEqual(res, "Wrong input parameters")

    def test_circ_perimeter_neg(self):
        res = perimeter(-123)
        self.assertEqual(res, "Wrong input parameters")


if __name__ == '__main__':
    unittest.main()
