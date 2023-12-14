import unittest
from Ploshad import Ploshad
from Ploshad import perimetr


class RectangleTestCase(unittest.TestCase):
    def test_zer0_mul(self):
        res = Ploshad(7, 3)
        self.assertEqual(res, 21)

    def test_pl_mul(self):
        res = Ploshad(2, 100000)
        self.assertEqual(res, 200000)

    def test_circ_perimeter_zero(self):
        res = perimetr(1, 2)
        self.assertEqual(res, 6)

    def test_circ_perimeter(self):
        res = perimetr(7, 1000000)
        self.assertEqual(res, 2000014)

    def test_circ_area_neg(self):
        res = Ploshad(-123, 0)
        self.assertEqual(res, "Change input parameters")

    def test_circ_perimeter_neg(self):
        res = perimetr(-123, 0)
        self.assertEqual(res, "Change input parameters")


if __name__ == '__main__':
    unittest.main()
