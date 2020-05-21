
from flask import Flask
from flask_migrate import Migrate, Manager, MigrateCommand
from flask_sessionstore import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_restful import Api


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_pyfile('../config_app.py')

    return app


app = create_app()

db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY']= db
session = Session(app)
csrf = CSRFProtect(app)
session.app.session_interface.db.create_all()


# Important thing is that we remove the CSRF for the API
api = Api(app, decorators=[csrf.exempt])

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
