import pytest 
import source.shapes as shapes

# like setup_method in class based testing. Now we can use it as a parameter in test_area in test_rectangle.py
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length = 10, width = 20)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(length = 5, width = 6)
