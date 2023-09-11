import abc
class Shape(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def calculate_area(self):
		pass

	@abc.abstractmethod
	def calculate_perimeter(self):
		pass