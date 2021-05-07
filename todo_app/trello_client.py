import json
from todo_app import trello_config
import requests


def get_cards(trello_config):
    url = f"{trello_config.base_url}/boards/{trello_config.board_id}/cards"
    query = {'key': trello_config.key, 'token': trello_config.token}
    response = requests.get(url = url, params = query)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a get cards request: {response.status_code}")
    return response.json()

def add_card(title,trello_config):
    querystring = {'name': title, 'idList': trello_config.todo_list_id, 'key': trello_config.key, 'token': trello_config.token}
    card_url = f"{trello_config.base_url}/cards/"
    response = requests.post(url = card_url, params=querystring)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a add card request: {response.status_code}")
def get_card_by_id(id):
    getcard = {'idList': trello_config.doing_list_id, 'key': trello_config.key, 'token': trello_config.token}
    get_card_url = f"{trello_config.base_url}/cards/{id}"
    response = requests.get(url = get_card_url, params=getcard)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a get card by id request: {response.status_code}")

def move_to_doing_card(id,trello_config):
    movequery = {'idList': trello_config.doing_list_id, 'key': trello_config.key, 'token': trello_config.token}
    move_url = f"{trello_config.base_url}/cards/{id}"
    response = requests.put(url= move_url, params = movequery)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a move card by id request: {response.status_code}")


def move_to_done_card(id,trello_config):
    donequery = {'idList': trello_config.done_list_id, 'key': trello_config.key, 'token': trello_config.token}
    done_url = f"{trello_config.base_url}/cards/{id}"
    response = requests.put(url= done_url, params = donequery)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a moved card by id request: {response.status_code}")

def undo_done_card(id,trello_config):
    undoquery = {'idList': trello_config.todo_list_id, 'key': trello_config.key, 'token': trello_config.token}
    undo_url = f"{trello_config.base_url}/cards/{id}"
    response = requests.put(url= undo_url, params = undoquery)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for a undo card by id from done request: {response.status_code}")

def create_trello_board(trello_config):
    create_board ={'key': trello_config.key, 'token': trello_config.token, 'name': trello_config.name}
    board_url = f"{trello_config.base_url}/boards/"
    response = requests.post(url=board_url, params = create_board)
        
    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for create board: {response.status_code}")
        
    print (response.text)
    board_json = response.json()
    return board_json['id']


def delete_trello_board(board_id,trello_config):
    delete_board ={'key': trello_config.key, 'token': trello_config.token}
    delete_url = f"{trello_config.base_url}/boards/{trello_config.board_id}"
    response = requests.delete(url=delete_url, params = delete_board)

    if response.status_code != 200:
        raise Exception(f"Wrong status code returned for create board: {response.status_code}")

    print (response.text)
