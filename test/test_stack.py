import pytest
from src import stack 

class TestStack:
    
    def test_push(self):
        stc1 = stack.Stack()
        assert stc1.is_empty() == True

        stc1.push(5)
        stc1.push(10)
        stc1.push(15)
        stc1.push(20)

        assert stc1.is_empty() == False
        assert stc1.get_stack_size() == 4
        assert stc1.get_peek_element() == 20
        assert stc1.get_all_stack_elements() == [5,10,15,20]

    def test_pop(self):
        stc1 = stack.Stack()
        assert stc1.is_empty() == True

        stc1.push(5)
        stc1.push(10)
        stc1.push(15)
        stc1.push(100)
        stc1.push(200)
        

        assert stc1.is_empty() == False
        assert stc1.get_stack_size() == 5
        assert stc1.get_peek_element() == 200
        assert stc1.get_all_stack_elements() == [5,10,15,100,200]

        result = stc1.pop()
        assert result == 200
        assert stc1.get_stack_size() == 4
        assert stc1.get_peek_element() == 100
        assert stc1.get_all_stack_elements() == [5,10,15,100]



    


        


