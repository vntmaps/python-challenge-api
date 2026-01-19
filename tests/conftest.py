import pytest

from main import create_app
from app.database import db
from app.models import Task

@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def seed_data(app):
    """Seed the database with initial tasks for GET testing."""
    with app.app_context():
        t1 = Task(title="Task One", status="pending")
        t2 = Task(title="Task Two", status="completed")
        db.session.add_all([t1, t2])
        db.session.commit()