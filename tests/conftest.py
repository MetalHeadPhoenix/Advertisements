import pytest
from src import create_app
from src.extensions import db

@pytest.fixture()
def app():
    app = create_app('config.Test')
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Creating all")
    

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()
        print("Dropping all")




@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
