from todo_app.view_model import ViewModel
from todo_app.todo_item import TodoItem

def test_view_model_todo_items():
    items = [
        TodoItem(1, "This is To Do Item", "To Do")
    ]
    todoitems = ViewModel.items

    assert todoitems
