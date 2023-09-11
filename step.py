from radish import given, when, then
from shapes import Rectangle

#rectangle = Rectangle(2, 3)

@given("Rectangle has {height:d} and {width:d} cm")
def have_initial(step, width, height):
     step.context.rectangle = Rectangle(width, height)

@when("I search area of rectangle")
def have_area(step):
    step.context.result = step.context.rectangle.calculate_area()
    
    
@then("I should have {result:d} with {height:d},{width:d}")
def should_result(step, result):    
    assert  step.context.result == result