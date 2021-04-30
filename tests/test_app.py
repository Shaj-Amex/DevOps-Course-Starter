from unittest.mock import patch
from todo_app import app
import pytest


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app
    test_app = todoapp.create_app()

    # Use the app to create a test_client
    with test_app.test_client() as client:
        yield client

def test_index_page(client):    
    response = client.get('/')