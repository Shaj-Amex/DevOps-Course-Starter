
from todo_app.trello_config import TrelloConfig
from flask import Flask, render_template, redirect, url_for, request,json
import requests
import os
import todo_app.trello_client as trello
from todo_app.todo_item import TodoItem
from todo_app.view_model import ViewModel

def create_app():

    app = Flask(__name__)
    trello_config = TrelloConfig()


    base_url = "https://api.trello.com/1/"
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('API_TOKEN')}


    @app.route('/')
    def index():
        raw_trello_cards = trello.get_cards(trello_config)
        items = [TodoItem.from_raw_trello_card(card) for card in raw_trello_cards]
        item_view_model = ViewModel(items)
        return  render_template('index.html',view_model=item_view_model)

    @app.route('/items/new', methods=['POST'])
    def add_item():
        name = request.form['title']
        trello.add_card(name,trello_config)
        return redirect("/")

    @app.route('/items/<id>/doing')
    def doing_item(id):
        trello.move_to_doing_card(id,trello_config)
        return redirect("/")

    @app.route('/items/<id>/done')
    def done_item(id):
        trello.move_to_done_card(id,trello_config)
        return redirect("/")

    @app.route('/items/<id>/undo')
    def undo_item(id):
        trello.undo_done_card(id,trello_config)
        return redirect("/")
    return app





 
