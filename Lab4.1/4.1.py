# Lab#4 - Boundary Value Analysis
# SC353201 Software Quality Assurance
# Semester 1/2567
# Instructor: Chitsutha Soomlek

import unittest

class Quadrilateral:
  """
  Represents a quadrilateral and provides methods to classify its type.
  """

  def __init__(self, top, left_side, bottom, right_side):
    """
    Initializes a Quadrilateral object with given side lengths.

    Args:
      top: Length of the top side.
      left_side: Length of the left side.
      bottom: Length of the bottom side.
      right_side: Length of the right side.

    Raises:
      ValueError: If any side length is not a positive number.
    """
    if top <= 0 or left_side <= 0 or bottom <= 0 or right_side <= 0:
      raise ValueError("Side lengths must be positive numbers.")

    self.top = top
    self.left_side = left_side
    self.bottom = bottom
    self.right_side = right_side

  def classify(self):
    """
    Classifies the type of quadrilateral based on its side lengths.

    Returns:
      A string describing the type of quadrilateral.
    """
    if self.top == self.bottom and self.left_side == self.right_side:
      if self.top == self.left_side:
        return "Square"
      else:
        return "Rectangle"
    elif self.top == self.bottom or self.left_side == self.right_side:
      return "Trapezoid" 
    else:
      return "Irregular"


top = float(input("Enter the length of the top side: "))
left_side = float(input("Enter the length of the left side: "))
bottom = float(input("Enter the length of the bottom side: "))
right_side = float(input("Enter the length of the right side: "))


try:
  quad = Quadrilateral(top, left_side, bottom, right_side)
except ValueError as e:
  print("Error:", e) 
else:
  quad_type = quad.classify()
  print("The shape is a:", quad_type)
    


class TestQuadrilateral(unittest.TestCase):

    def run_test(self, top, left, bottom, right, expected):
        quad = Quadrilateral(top, left, bottom, right)
        result = quad.classify()
        self.assertEqual(result, expected)

    def test_square_minimum(self):
        self.run_test(1, 1, 1, 1, "Square")
        
    def test_square_typical(self):
        self.run_test(10, 10, 10, 10, "Square")

    def test_square_maximum(self):
        self.run_test(9999, 9999, 9999, 9999, "Square")

    def test_rectangle_minimum(self):
        self.run_test(1, 2, 1, 2, "Rectangle")

    def test_rectangle_typical(self):
        self.run_test(5, 10, 5, 10, "Rectangle")

    def test_rectangle_maximum(self):
        self.run_test(9998, 9999, 9998, 9999, "Rectangle")

    def test_trapezoid_minimum(self):
        self.run_test(1, 2, 1, 3, "Trapezoid")

    def test_trapezoid_typical(self):
        self.run_test(5, 10, 5, 15, "Trapezoid")

    def test_trapezoid_maximum(self):
        self.run_test(9997, 9998, 9997, 9999, "Trapezoid")

    def test_irregular_minimum(self):
        self.run_test(1, 2, 3, 4, "Irregular")

    def test_irregular_typical(self):
        self.run_test(5, 7, 9, 11, "Irregular")

    def test_irregular_maximum(self):
        self.run_test(9996, 9997, 9998, 9999, "Irregular")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            Quadrilateral(0, 1, 1, 1)
        print("Test: Quadrilateral(0, 1, 1, 1) raises ValueError")

if __name__ == '__main__':
    unittest.main()
