import os

class TrelloConfig:
    def __init__(self):
        self.base_url = "https://api.trello.com/1"
        self.board_id = os.getenv('BOARD_ID')
        self.name = os.getenv('NAME')
        self.key = os.getenv('API_KEY')
        self.token = os.getenv('API_TOKEN')
        self._todo_list_id = os.getenv('TODO_LIST_ID')
        self._doing_list_id = os.getenv('DOING_LIST_ID')
        self._done_list_id = os.getenv('DONE_LIST_ID')

    @property
    def todo_list_id(self):
        todo_list_id = self._todo_list_id
        return todo_list_id
    @property
    def doing_list_id(self):
        doing_list_id = self._doing_list_id
        return doing_list_id
    @property
    def done_list_id(self):
        done_list_id = self._done_list_id
        return done_list_id
    

        
