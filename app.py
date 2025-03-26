from flask import Flask
from storage.sqlite_data_manager import data_manager, db, UserAccount, Movie


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = data_manager.db_file_name
db.init_app(app)

with app.app_context():
    db.create_all()