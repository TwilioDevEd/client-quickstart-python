import os
import pytest

from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    return app.test_client()
