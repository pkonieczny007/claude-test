from flask import Flask

from claude_test.models import db
from claude_test.routes import register_routes


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///claude_test.db"

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)
    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
