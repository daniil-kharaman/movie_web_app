from flask_sqlalchemy import SQLAlchemy
from data_manager_interface import DataManagerInterface

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db = SQLAlchemy(db_file_name)

        