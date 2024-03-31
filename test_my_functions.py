import pytest
import time
import my_functions as my_functions

def test_add():
    result = my_functions.add(3,4)
    assert result == 5

def test_divide():
    result = my_functions.divide(4,5)
    assert result == -2

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(4,5)
    assert result == -2

@pytest.mark.skip(reason="this feature is currently broken")
def test_add():
    assert my_functions.add(1,2) ==3

@pytest.mark.xfail(reason="we know we cannnot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4,0)