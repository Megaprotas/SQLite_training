import sqlite3

from typing import List, Dict, Union

from .db_connections import DatabaseConnection

db_file = 'data.db'

Game = Dict[str, Union[str, int]]


def create_games_table() -> None:           # expected return None
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS games(name text primary key, studio text, played integer)')


def add_game_db(name: str, studio: str) -> None:
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        try:
            cursor.execute(f'INSERT INTO games VALUES(?, ?, 0)', (name, studio))
        except sqlite3.IntegrityError:
            print('Name already exists on db')


def games_list() -> List[Game]:
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM games')
        games = [{'name': row[0], 'studio': row[1], 'played': row[2]} for row in cursor.fetchall()]

        return games


def mark_as_played_in_db(name: str) -> None:
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE games SET played=1 WHERE name=?', (name,))


def delete_game_from_db(name: str) -> None:
    with DatabaseConnection(db_file) as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM games WHERE name=?', (name,))




