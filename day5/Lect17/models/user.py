"""Модуль содержащий описание класса User."""
import sqlite3


class User:
    __tablename__ = "users"
    __dbname__ = "data.db"
    """
    Класс, описывающий пользователя
    attrs:
        * login - str ...
        * password - str ..
        * about - str ...
    """

    def __init__(self, login: str, password: str, about: str):
        self.__login = login
        self.__password = password
        self.__about = about

    def save(self):
        """Метод для сохранения юзера в таблице"""
        conn = sqlite3.connect(self.__dbname__)
        cur = conn.cursor()

        insert_query = f"INSERT INTO {self.__tablename__} VALUES(NULL, ?, ?, ?)"
        cur.execute(
            insert_query,
            (self.__login, self.__password, self.__about),
        )

        conn.commit()
        conn.close()

    @classmethod
    def all(cls):
        """Метод, возвращающий всех пользователей из таблицы"""
        conn = sqlite3.connect(cls.__dbname__)
        cur = conn.cursor()
        select_query = f"SELECT * FROM {cls.__tablename__}"
        users = []
        for user_row in cur.execute(select_query):
            users.append(
                cls(login=user_row[1], password=user_row[2], about=user_row[3])
            )
        conn.commit()
        conn.close()
        return users

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def about(self):
        return self.__about

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"User (Login:{self.__login}, About:{self.__about})"
