Feature: Rectangle
    Scenario: Arguments for given, when, then
        Given Rectangle has 2 and 3 cm
        When I search area of rectangle 2 * 3
        Then I should have 6
       