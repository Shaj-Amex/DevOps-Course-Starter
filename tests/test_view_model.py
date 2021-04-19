from todo_app.view_model import ViewModel
from todo_app.todo_item import TodoItem

def test_view_model_todo_items():
    items = [
        TodoItem(1, "This is To Do Item", "To Do")
    ]
    todoitems = ViewModel.todo_items

    assert todoitems

def test_view_model_doing_items():
    items = [
        TodoItem(1, "This is Doing Item", "Doing")
    ]
    doingitems = ViewModel.doing_items

    assert doingitems

def test_view_model_done_items():
    items = [
        TodoItem(1, "This is Done Item", "Done")
    ]
    doneitems = ViewModel.doing_items

    assert doneitems



