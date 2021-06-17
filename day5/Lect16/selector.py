import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Вытаскиваем все элементы таблицы
select_query = "SELECT * FROM books"
rows = cur.execute(select_query)
count = 0
print("QUERY:", select_query)
for row in rows:
    count+=1
    print(row)
    if count > 10:
        break

select_query_if = "SELECT * FROM books WHERE id < 10"
rows = cur.execute(select_query_if)
print("QEURY:", select_query_if)
for row in rows:
    print(row)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()