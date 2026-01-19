from flask import Flask
from app.database import db
from app.routes import task_bp

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'postgresql://user:password@localhost:5432/task_db'

    db.init_app(app)
    app.register_blueprint(task_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)