from storage.data_manager_interface import DataManagerInterface
from sqlalchemy import text, exc
import os


class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name, db_path, user_model, movie_model, db):
        self.db_file_name = db_file_name
        self.db_path = db_path
        self.user_model = user_model
        self.movie_model = movie_model
        self.db = db


    def check_database_connection(self):

        """Checks if the database file exists and verifies that a connection to the database can be established."""

        if not os.path.exists(self.db_path):
            print(f"Database file was not found: {self.db_path}")
            return False
        try:
            self.db.session.execute(text('SELECT 1'))
            print('Connection established')
            return True
        except (exc.OperationalError, Exception) as e:
            print(f"Impossible to connect with the database: {e}")
            return False


    def get_all_users(self):

        """Retrieves all user accounts from the database."""

        return self.db.session.execute(self.db.select(self.user_model)).scalars()


    def get_user_movies(self, user_id):

        """Fetches all movies associated with a given user ID from the database."""

        return self.db.session.execute(self.db.select(self.movie_model).where(self.movie_model.user_id == user_id)).scalars()


    def get_movie_by_id(self, movie_id):

        """Retrieves a movie record from the database by its movie ID."""

        return self.db.session.get(self.movie_model, movie_id)


    def add_user(self, name):

        """Creates and adds a new user account with the given name to the database."""

        user = self.user_model(
            name=name,
        )
        self.db.session.add(user)
        self.db.session.commit()


    def delete_user(self, user_id):

        """Deletes the user account identified by the given user ID from the database."""

        user = self.db.session.get(self.user_model, user_id)
        self.db.session.delete(user)
        self.db.session.commit()


    def update_user(self, user_id, new_name):

        """Updates the name of an existing user account specified by the user ID."""

        user = self.db.session.get(self.user_model, user_id)
        user.name = new_name
        self.db.session.commit()


    def add_movie(self, title, user_id, director, year, rating, poster):

        """Adds a new movie record with the provided details for a specific user to the database."""

        movie = self.movie_model(
            title=title,
            director=director,
            year=year,
            rating=rating,
            poster=poster,
            user_id=user_id
        )
        self.db.session.add(movie)
        self.db.session.commit()


    def delete_movie(self, movie_id):

        """Removes a movie record from the database using the specified movie ID."""

        movie = self.db.session.get(self.movie_model, movie_id)
        self.db.session.delete(movie)
        self.db.session.commit()


    def update_movie(self, movie_id, title, director, year, rating, poster):

        """Updates an existing movie record with new information including title, director, year, rating, and poster."""

        movie = self.db.session.get(self.movie_model, movie_id)
        movie.title = title
        movie.director = director
        movie.year = year
        movie.rating = rating
        movie.poster = poster
        self.db.session.commit()


    def user_in_database(self, user_name):

        """Checks if a user with the specified name exists in the database."""

        if not self.db.session.execute(self.db.select(self.user_model).where(self.user_model.name == user_name)).all():
            return False
        return True


    def movie_in_database(self, movie_title, user_id):

        """Checks if a movie with the specified title exists for the given user ID in the database."""

        if not self.db.session.execute(self.db.select(self.movie_model).\
                                               where(self.movie_model.title == movie_title,
                                                     self.movie_model.user_id == user_id)).all():
            return False
        return True
