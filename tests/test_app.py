from unittest.mock import patch

from todo_app import app
import pytest
from dotenv import find_dotenv, load_dotenv


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app
    test_app = app.create_app()

    # Use the app to create a test_client
    with test_app.test_client() as client:
        yield client

def test_index_page(client):    
    response = client.get('/')