# (venv)...\PyTest\tests> pytest test_my_functions.py
import pytest
import source.my_functions as my_functions
import time 

def test_add():
    # 1 + 4 = 5
    result = my_functions.add(number_one = 1, number_two = 4)
    assert result == 5


def test_add_strings():
    result = my_functions.add(number_one = "Hello ", number_two = "World!")
    assert result == "Hello World!"


def test_divide():
    # 10 / 5 = 2
    result = my_functions.divide(number_one = 10, number_two = 5)
    assert result == 2


def test_divide_by_zero():
    # 10 / 0 = undefined (is what we are expecting)
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(number_one = 10, number_two = 0)

# (venv)...\PyTest\tests>pytest -m slow
@pytest.mark.slow
def test_very_slow():
    time.sleep(3) # sleep for 3 seconds
    # 10 / 5 = 2
    result = my_functions.divide(number_one = 10, number_two = 5)
    assert result == 2

# flag -> s
@pytest.mark.skip(reason = "This feature is currently broken")
def test_add():
    result = my_functions.divide(number_one = 10, number_two = 5)
    assert result == 2

# flag -> x
@pytest.mark.xfail(reason = "We know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(number_one = 4, number_two = 0)