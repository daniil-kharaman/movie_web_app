from flask_sqlalchemy import SQLAlchemy
from storage.data_manager_interface import DataManagerInterface
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

DATABASE_URL = 'sqlite:////Users/daniilkharaman/python/movieweb_app/database/data.db'

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name
        self.db = SQLAlchemy()


    def get_all_users(self):
        return self.db.session.execute(self.db.select(UserAccount)).scalars()


    def get_user_movies(self, user_id):
        return self.db.session.execute(self.db.select(Movie).where(Movie.user_id == user_id)).scalars()


    def add_user(self, name):
        user = UserAccount(
            name=name,
        )
        self.db.session.add(user)
        self.db.session.commit()


    def delete_user(self, user_id):
        user = self.db.session.get(UserAccount, user_id)
        self.db.session.delete(user)
        self.db.session.commit()


    def update_user(self, user_id, new_name):
        user = self.db.session.get(UserAccount, user_id)
        user.name = new_name
        self.db.session.commit()


    def add_movie(self, title, director, year, rating, user_id):
        movie = Movie(
            title=title,
            director=director,
            year=year,
            rating=rating,
            user_id=user_id
        )
        self.db.session.add(movie)
        self.db.session.commit()


    def delete_movie(self, movie_id):
        movie = self.db.session.get(Movie, movie_id)
        self.db.session.delete(movie)
        self.db.session.commit()


    def update_movie(self, movie_id, title=None, director=None, year=None, rating=None):
        movie = self.db.session.get(Movie, movie_id)
        if title:
            movie.title = title
        if director:
            movie.director = director
        if year:
            movie.year = year
        if rating:
            movie.rating = rating
        self.db.session.commit()

data_manager = SQLiteDataManager(DATABASE_URL)
db = data_manager.db


class UserAccount(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    movies: Mapped[List['Movie']] = relationship(back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"UserAccount(id={UserAccount.id}, name={UserAccount.name})"


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    director: Mapped[Optional[str]]
    year: Mapped[Optional[int]]
    rating: Mapped[Optional[int]]
    user_id: Mapped[int] = mapped_column(ForeignKey('user_account.id'))
    user : Mapped['UserAccount'] = relationship(back_populates='movies')

    def __repr__(self):
        return (f"Movie(id={Movie.id}, title={Movie.title}, director={Movie.director},"
                f"year={Movie.year}, rating={Movie.rating})")