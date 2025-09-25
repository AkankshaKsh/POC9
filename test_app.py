import unittest
import app
class TestCalculator(unittest.TestCase):
   def test_add(self):
       self.assertEqual(app.add_numbers(2, 3), 5)
   def test_subtract(self):
       self.assertEqual(app.subtract_numbers(10, 4), 6)
   def test_multiply(self):
       self.assertEqual(app.multiply_numbers(3, 7), 21)
   def test_divide(self):
       self.assertEqual(app.divide_numbers(8, 2), 4)
   def test_divide_by_zero(self):
       self.assertEqual(app.divide_numbers(5, 0), "Error: Division by zero")
if __name__ == "__main__":
   unittest.main()
