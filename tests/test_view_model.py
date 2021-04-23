from todo_app.view_model import ViewModel
from todo_app.todo_item import TodoItem

def test_view_model_todo_items():
    items = [
        TodoItem(1, "To Do", "This is To Do Item"),
        TodoItem(2,  "Doing", "This is Doing Item"),
        TodoItem(3,  "Done",  "This is Done")
    ]
    viewmodel = ViewModel(items)
    todoitems = viewmodel.todo_items

    assert len(todoitems) == 1 
    item = todoitems[0]
    assert item.status == 'To Do'

def test_view_model_doing_items():
    items = [
        TodoItem(1, "Doing", "This is Doing Item"),
        TodoItem(2,  "To Do", "This is Doing Item"),
        TodoItem(3,  "Done",  "This is Done")
    ]
    viewmodel = ViewModel(items)
    doingitems = viewmodel.doing_items

    assert len(doingitems) == 1
    item = doingitems[0]
    assert item.status == 'Doing'


def test_view_model_done_items():
    items = [
         TodoItem(1, "Done", "This is Done Item"),
        TodoItem(2,  "To Do", "This is Doing Item"),
        TodoItem(3,  "Doing",  "This is Doing")
    ]
    viewmodel = ViewModel(items)
    doneitems = viewmodel.done_items

    assert len(doneitems)  == 1
    item = doneitems[0]
    assert item.status == 'Done'



