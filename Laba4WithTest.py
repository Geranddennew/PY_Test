from TDD import TestShapeFunctions
from shapes import Rectangle, Square
from shapes import Circle
from ShapeFactory import ShapeFactory
from Shape import Shape
from pytest_bdd import scenarios, given, when, then, parsers

import unittest

def main():

	shape_factory = ShapeFactory()
	shape_name = input("Enter the name of the shape: ")

	shape = shape_factory.create_shape(shape_name)

	print(f"The type of object created: {type(shape)}")
	print(f"The area of the {shape_name} is: {shape.calculate_area()}")
	print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")




if __name__ == '__main__': 
	main()
