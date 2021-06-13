import os
import pytest
import dotenv
from todo_app import app
from todo_app.trello_config import  TrelloConfig
from todo_app.trello_client import create_trello_board,delete_trello_board, get_doing_lists_on_board, get_todo_lists_on_board
from todo_app.trello_client import get_done_lists_on_board                        
from threading import Thread
from selenium import webdriver 
import time

@pytest.fixture(scope='module')
def app_with_temp_board(): 
    file_path = dotenv.find_dotenv('.env')
    dotenv.load_dotenv(file_path, override=True)
    config = TrelloConfig()
   
    # Create the new board & update the board id environment variable
    board_id = create_trello_board(config)
    os.environ['BOARD_ID'] = board_id

    # Get the Todo List ID, Doing List Id and Done List Id from Board
    config = TrelloConfig()
    todo_list_id = get_todo_lists_on_board(board_id,config)
    os.environ['TODO_LIST_ID'] = todo_list_id
    config = TrelloConfig()
    doing_list_id = get_doing_lists_on_board(board_id,config)
    os.environ['DOING_LIST_ID'] = doing_list_id
    config = TrelloConfig()
    done_list_id = get_done_lists_on_board(board_id,config)
    os.environ['DONE_LIST_ID'] = done_list_id
    

    # construct the new application    
    application = app.create_app()

    #start the app in its own thread.    
    thread = Thread(target=lambda: application.run(use_reloader=False))    
    thread.daemon = True    
    thread.start()    
    yield application

    # Tear Down
    thread.join(1)
    delete_trello_board(board_id,config)

@pytest.fixture(scope="module")
def driver():  
    
    with webdriver.Chrome(executable_path=r'/Users/shajeethsushama/DevOps-Course-Starter/chromedriver') as driver:
        yield driver

def test_task_journey(driver, app_with_temp_board):   
    driver.get('http://localhost:5000/') 
    time.sleep(30) 
    assert driver.title == 'To-Do App'