"""Programmatically creating function to iterate process to interact with db"""


import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

GET_CHARACTERS = """
SELECT
    COUNT(DISTINCT name) AS items_count
FROM
    armory_item
"""
# Right SQL Needed
# The """ """ (docstrings) also can support multi-line functionality as such:


if __name__ == '__main__':
    connection = connect_to_db()
    cursor = connection.cursor()
    results = execute_query(cursor, GET_CHARACTERS)
    print(results)