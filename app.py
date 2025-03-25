from flask import Flask
from storage.sqlite_data_manager import SQLiteDataManager
DATABASE_FILE = 'sqlite:////database/data.db'

app = Flask(__name__)
db = SQLiteDataManager(DATABASE_FILE).db
db.init_app(app)