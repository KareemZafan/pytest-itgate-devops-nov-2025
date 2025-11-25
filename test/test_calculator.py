import pytest
from src import calculator as calc

test_data_sub = [(8,3,5), (-1,1,-2), (-11,-20,9), (-11,0,-11), (0,0,0), (100,50,50), (2.5,1.5,1.0)]
test_data_add = [(8,3,11), (-1,1,0), (-11,-20,-31), (-11,0,-11), (100,50,150), (2.5,1.5,4.0)]

@pytest.mark.JANUARY
@pytest.mark.parametrize("input1,input2,result", test_data_add)
def test_add(input1, input2, result):
    assert calc.add(input1, input2) == result 
    
@pytest.mark.parametrize("input1,input2,result", test_data_sub)
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
