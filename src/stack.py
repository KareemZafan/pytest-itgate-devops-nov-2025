
class Stack: 
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def get_stack_size(self):
        return len(self.items)
    
    def push(self, value):
        self.items.append(value)

    def get_peek_element(self):
        return self.items[-1]

    def pop(self):
        popped_item = self.get_peek_element()
        self.items.remove(popped_item)
        return popped_item
    
    def get_all_stack_elements(self):
        return self.items
    

    

        

