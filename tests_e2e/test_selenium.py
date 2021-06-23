import os
import pytest
from dotenv import find_dotenv, load_dotenv
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from todo_app import app
from todo_app.trello_config import  TrelloConfig
from todo_app.trello_client import create_trello_board,delete_trello_board, get_doing_lists_on_board, get_todo_lists_on_board
from todo_app.trello_client import get_done_lists_on_board                        
from threading import Thread
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
import time

@pytest.fixture(scope='module')
def app_with_temp_board(): 
    
    try:
        file_path = find_dotenv('.env')
        load_dotenv(file_path, override=True)
    except OSError:
        print('Failed to load dotenv, continuing...')

    #load_dotenv(file_path, override=True)

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
# Below Code for Running on Docker in Headless Mode
def driver():  
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('/usr/bin/chromedriver', options=opts) as driver:
       yield driver
# Uncomment Below Code for Running on Local
#@pytest.fixture(scope="module")
#def driver():  
#     with webdriver.Chrome('./chromedriver') as driver:
#       yield driver
        

def test_task_journey(driver: WebDriver, app_with_temp_board): 
    driver.get('http://localhost:5000/') 
    assert driver.title == 'To-Do App'
    time.sleep(1)
    text_box:WebElement = driver.find_element_by_name('title')
    text_box.send_keys("Test Todo")
    time.sleep(1)
    submit_button: WebElement = driver.find_element_by_name('submit')
    submit_button.click()
    time.sleep(1)
    doing_button: WebElement = driver.find_element_by_name('doing-button')
    doing_button.click()
    time.sleep(1)
    done_button: WebElement = driver.find_element_by_name('done-button')
    done_button.click()
    time.sleep(1)
    item_text: WebElement = driver.find_element_by_name('item-text')
    assert item_text.text == 'Test Todo - Done'  
