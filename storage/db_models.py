from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from sqlalchemy import ForeignKey
db = SQLAlchemy()
model = db.Model



class UserAccount(model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)
    movies: Mapped[List['Movie']] = relationship(back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"UserAccount(id={UserAccount.id}, name={UserAccount.name})"


class Movie(model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    director: Mapped[Optional[str]]
    year: Mapped[Optional[int]]
    rating: Mapped[Optional[float]]
    poster: Mapped[Optional[str]]
    user_id: Mapped[int] = mapped_column(ForeignKey('user_account.id'))
    user : Mapped['UserAccount'] = relationship(back_populates='movies')

    def __repr__(self):
        return (f"Movie(id={Movie.id}, title={Movie.title}, director={Movie.director},"
                f"year={Movie.year}, rating={Movie.rating})")