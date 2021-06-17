import sqlite3 

# Установка подключения к бд
conn = sqlite3.connect("data.db")

# Создание интерфейса взаимодействия с базой
cur = conn.cursor()

# Выполнение запросов
cur.execute()

# Подтверждение запроса
conn.commit()

# Закроем соединение
conn.close()

