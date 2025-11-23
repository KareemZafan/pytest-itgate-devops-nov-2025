import pytest

day = 29
def test_upper():
    assert 'foo'.upper() == 'FOO'

@pytest.mark.JANUARY
def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()

@pytest.mark.skip(reason="Not implemented yet")
def test_capitalize():
    assert 'hello world'.capitalize() == 'Hello world'
    assert 'python'.capitalize() == 'Python'    

def test_title():
    assert 'hello world'.title() == 'Hello World'
    assert 'python programming'.title() == 'Python Programming'

@pytest.mark.JANUARY
def test_contains():
    assert 'hello'.__contains__('he')
    assert 'she is ready'.__contains__('she')

@pytest.mark.skipif(day<28, reason="Test skipped for the first days of the month")
def test_bill_payement():
    print("\nBill payment test executed\n")
    