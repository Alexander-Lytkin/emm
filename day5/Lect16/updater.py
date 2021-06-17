import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

update_query = "UPDATE books SET author = 'J. Jr. Talkin' WHERE author = 'J.J.Talkin'"
cur.execute(update_query)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()