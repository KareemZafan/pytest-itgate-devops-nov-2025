import pytest
from src import calculator as calc

test_data = [(8,3,5), (-1,1,-2), (-11,-20,9), (-11,0,-11), (0,0,0), (100,50,50), (2.5,1.5,1.0)]

@pytest.mark.JANUARY
def test_add():
    assert calc.add(2,3) == 5
    assert calc.add(-1,1) == 0
    assert calc.add(-11,-20) == -31
    assert calc.add(-11,0) == -11
    
@pytest.mark.parametrize("input1,input2,result", test_data)
def test_subtract(input1, input2, result):
    assert calc.subtract(input1, input2) == result

def test_multiply():
    assert calc.multiply(2,3) == 6
    assert calc.multiply(-1,1) == -1
    assert calc.multiply(-11,-20) == 220
    assert calc.multiply(-11,0) == 0

@pytest.mark.JANUARY
def test_divide():
    assert calc.divide(6,3) == 2
    assert calc.divide(-6,2) == -3
    assert calc.divide(-20,-5) == 4
    assert calc.divide(0,5) == 0
    assert calc.divide(5,0) is None 

def printHello():
    print("Hello, World!")    
