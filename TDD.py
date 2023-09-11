from shapes import Rectangle, Square
from shapes import Circle
import unittest


class TestShapeFunctions(unittest.TestCase):
	def test_calculate_area_of_rectangle(self):
		rec = Rectangle(2, 2)
		self.assertEqual(rec.calculate_area(), 4, "Should be 4")

	def test_calculate_perimeter_of_rectangle(self):
		rec = Rectangle(2, 2)
		self.assertEqual(rec.calculate_perimeter(), 8, "Should be 8")

	def test_calculate_area_of_Square(self):
		square = Square(2)
		self.assertEqual(square.calculate_area(), 4, "Should be 4")

	def test_calculate_perimeter_of_Square(self):
		square = Square(2)
		self.assertEqual(square.calculate_perimeter(), 8, "Should be 8")
		
	def test_calculate_area_of_circle(self):
		circle = Circle(2)
		self.assertEqual(circle.calculate_area(), 12.56, "Should be 12.56")

	def test_calculate_perimeter_of_circle(self):
		circle = Circle(2)
		self.assertEqual(circle.calculate_area(), 12.56, "Should be 12.56")


suite = unittest.TestLoader().loadTestsFromTestCase(TestShapeFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)