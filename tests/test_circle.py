# (venv) ...\PyTest\tests> pytest test_circle.py
# pytest -s  --> to see the print statement executions 

import pytest 
import source.shapes as shapes
import math 

class TestCircle:
    
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_area(self):
        expected_value = math.pi * self.circle.radius**2
        assert self.circle.area() == expected_value

    def test_perimeter(self):
        expected_value = 2 * math.pi * self.circle.radius
        assert self.circle.perimeter() == expected_value

    def test_not_equal(my_rectangle, weird_rectangle):
        assert my_rectangle != weird_rectangle

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()