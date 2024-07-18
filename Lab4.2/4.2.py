import unittest
import math

class Quadrilateral:
    def __init__(self, top, left_side, bottom, right_side):
        if top <= 0 or left_side <= 0 or bottom <= 0 or right_side <= 0:
            raise ValueError("Side lengths must be positive numbers.")
        self.top = top
        self.left_side = left_side
        self.bottom = bottom
        self.right_side = right_side

    def classify(self):
        if self.top == self.bottom and self.left_side == self.right_side:
            if self.top == self.left_side:
                return "Square"
            else:
                return "Rectangle"
        elif self.top == self.bottom or self.left_side == self.right_side:
            return "Trapezoid" 
        else:
            return "Irregular"

class TestQuadrilateralRobust(unittest.TestCase):

    def test_valid_cases(self):
        test_cases = [
            ((5, 5, 5, 5), "Square"),
            ((4, 3, 4, 3), "Rectangle"),
            ((4, 3, 4, 5), "Trapezoid"),
            ((2, 3, 4, 5), "Irregular"),
        ]
        for sides, expected in test_cases:
            with self.subTest(sides=sides):
                quad = Quadrilateral(*sides)
                self.assertEqual(quad.classify(), expected)

    def test_invalid_input(self):
        invalid_inputs = [
            (0, 1, 1, 1), (-1, 1, 1, 1), (1, 0, 1, 1), (1, -1, 1, 1),
            (1, 1, 0, 1), (1, 1, -1, 1), (1, 1, 1, 0), (1, 1, 1, -1),
        ]
        for sides in invalid_inputs:
            with self.subTest(sides=sides):
                with self.assertRaises(ValueError):
                    Quadrilateral(*sides)

    def test_boundary_values(self):
        test_cases = [
            ((0.0001, 0.0001, 0.0001, 0.0001), "Square"),
            ((9999999999, 9999999999, 9999999999, 9999999999), "Square"),
            ((1, 9999999999, 1, 9999999999), "Rectangle"),
            ((0.0001, 1, 0.0001, 2), "Trapezoid"),
        ]
        for sides, expected in test_cases:
            with self.subTest(sides=sides):
                quad = Quadrilateral(*sides)
                self.assertEqual(quad.classify(), expected)

    def test_almost_equal_sides(self):
        test_cases = [
            ((1, 1, 1, 1.0001), "Irregular"),
            ((1, 1, 1.0001, 1), "Trapezoid"),
            ((1, 1.0001, 1, 1.0001), "Rectangle"),
        ]
        for sides, expected in test_cases:
            with self.subTest(sides=sides):
                quad = Quadrilateral(*sides)
                self.assertEqual(quad.classify(), expected)

    def test_floating_point_precision(self):
        sides = (0.3, 0.3, 0.3, 0.3)
        quad = Quadrilateral(*sides)
        self.assertEqual(quad.classify(), "Square")

    def test_very_large_difference(self):
        quad = Quadrilateral(1, 1000000000, 1, 1000000000)
        self.assertEqual(quad.classify(), "Rectangle")

    def test_non_euclidean_sides(self):
        quad = Quadrilateral(3.14159, 2.71828, 1.41421, 2.30259)
        self.assertEqual(quad.classify(), "Irregular")

if __name__ == '__main__':
    unittest.main()
