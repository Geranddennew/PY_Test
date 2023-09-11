from shapes import Circle
from shapes import Rectangle
from shapes import Square
class ShapeFactory:
	def create_shape(self, name):
		if name == 'circle':
			radius = input("Enter the radius of the circle: ")
			return Circle(float(radius))

		elif name == 'rectangle':
			height = input("Enter the height of the rectangle: ")
			width = input("Enter the width of the rectangle: ")
			return Rectangle(int(height), int(width))

		elif name == 'square':
			width = input("Enter the width of the square: ")
			return Square(int(width))