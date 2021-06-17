import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Запрос на создание таблицы books
create_query = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)"
# Выполнеине запроса на создание таблицы books
cur.execute(create_query)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()