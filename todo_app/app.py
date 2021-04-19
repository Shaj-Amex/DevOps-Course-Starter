
from flask import Flask, render_template, redirect, url_for, request,json
import requests
import os
import todo_app.trello_client as trello
from todo_app.todo_item import TodoItem
from todo_app.view_model import ViewModel

app = Flask(__name__)


base_url = "https://api.trello.com/1/"
query = {'key': os.getenv('API_KEY'), 'token': os.getenv('API_TOKEN')}


@app.route('/')
def index():
    raw_trello_cards = trello.get_cards()
    items = [TodoItem.from_raw_trello_card(card) for card in raw_trello_cards]
    item_view_model = ViewModel(items)
    return  render_template('index.html',view_model=item_view_model)

@app.route('/items/new', methods=['POST'])
def add_item():
    name = request.form['title']
    trello.add_card(name)
    return redirect("/")

@app.route('/items/<id>/doing')
def doing_item(id):
    trello.move_to_doing_card(id)
    return redirect("/")

@app.route('/items/<id>/done')
def done_item(id):
    trello.move_to_done_card(id)
    return redirect("/")

@app.route('/items/<id>/undo')
def undo_item(id):
    trello.undo_done_card(id)
    return redirect("/")

if __name__ == '__main__':
    app.run()


 
