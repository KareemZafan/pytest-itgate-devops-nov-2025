import pytest

"""@pytest.fixture
def open_DB_connection(): 
    print("\nOpen DB Connection\n")


@pytest.fixture
def close_DB_connection(): 
    yield
    print("\nClose DB Connection\n")   """

@pytest.fixture(autouse=True,scope='module')
def setup_DB_connection():
     print("\nOpen DB Connection\n")
     yield
     print("\nClose DB Connection\n")


def test_insertion_row_DB():
    print("\nInserting ...\n")
    
def test_updating_row_DB():
    print("\nUpdating ...\n")

def test_deleting_row_DB():
    print("\nDeleting ...\n")