import pytest
import source.shapes as shapes

# parametrize decorator is used to pass multiple values to the test function. side_length refers to 5, 4, and 9. expected_area refers to 25, 16, and 81.
@pytest.mark.parametrize("side_length, expected_area", 
                        [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", 
                        [(3, 12), (4, 16), (5, 20)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter

