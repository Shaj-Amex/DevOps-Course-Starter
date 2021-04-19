class ViewModel:
    def __init__(self,items):
        self._items = items
    
    @property
    def items(self):
        return self.items

    @property
    def todo_items(self):
        todoitems = [x for x in self._items if x.status == 'To Do'] 
        return todoitems

    @property
    def doing_items(self):
        return self._items

    @property
    def done_items(self):
        return self._items

