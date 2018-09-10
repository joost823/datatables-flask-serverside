from flask import Flask
from flask_sqlalchemy import SQLAlchemy


flask_app = Flask(__name__)
db = SQLAlchemy(flask_app)

from app.mod_tables.models import TableBuilder, SomeTable, add_some_random_db_entries

db.create_all()

add_some_random_db_entries()

table_builder = TableBuilder()


from app.common.routes import main
from app.mod_tables.controllers import tables


# Register the different blueprints
flask_app.register_blueprint(main)
flask_app.register_blueprint(tables)
