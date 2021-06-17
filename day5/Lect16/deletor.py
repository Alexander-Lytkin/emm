import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

delete_query = "DELETE FROM books"
cur.execute(delete_query)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()