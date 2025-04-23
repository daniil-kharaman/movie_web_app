from storage.sqlite_data_manager import SQLiteDataManager
from storage.db_models import UserAccount, Movie, db

db_path = '/Users/daniilkharaman/python/movieweb_app/database/data2.db'
DATABASE_URL = f"sqlite:///{db_path}"

data_manager = SQLiteDataManager(DATABASE_URL, db_path, user_model=UserAccount, movie_model=Movie, db=db)
