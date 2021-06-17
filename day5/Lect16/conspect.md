### Лекция 16. sqlite3

***SQLite*** - это реляционная встраиваемая СУБД, которая отличается досттаочно минималистичным набором поддерживаемых типов.

В ```python``` интерпретатор встроен движок ```sqlite```.

### Шаг 1. Основные команды
* 1) Установка подключения/создание интерфейса
* 2) Выполнение запроса
* 3) Подтверждение запроса
* 4) Отключение

```
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


```

### Шаг 2. Создание таблицы
* Первым делом нужно попродить схему таблицы
* Допустим хотим сохранить книжки
```
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
```

### Шаг 3. Добавление новых строк в таблицу
* Хотим добавить 1 книгу
* Хотим добавить сразу несколько книг
```
import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

# Одна книга для добавления
one_book = ("HP:2", "J.Rawling")
# Набор книг для добавления
many_books = [
    ("LOTR:1", "J.J.Talkin"),
    ("LOTR:2", "J.J.Talkin"),
    ("LOTR:3", "J.J.Talkin"),
    ] * 50

# '?' - placeholder - место, куда мы подставим данные в ходе выполнения запроса
insert_query = "INSERT INTO books (id, title, author) VALUES(NULL, ?, ?)"
# Способ добавления одной книги
cur.execute(insert_query, one_book)
# Способ добавления нескольких книг
# for book in many_books:
#     cur.execute(insert_query, book)
#     conn.commit()
cur.executemany(insert_query, many_books)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()
```

### Шаг 4. Получение данных
* Хотим получить все книги
* Хотим найти какую-то определенную книгу
```
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
```

### Шаг 5. Обновление элементов
* Хотим поменять имена авторов
```
import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

update_query = "UPDATE books SET author = 'J. Jr. Talkin' WHERE author = 'J.J.Talkin'"
cur.execute(update_query)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()
```

### Шаг 6. Удаление
* Хотим удалить все вторые тома какой-то книги
```
import sqlite3


conn = sqlite3.connect("data.db")
cur = conn.cursor()

delete_query = "DELETE FROM books"
cur.execute(delete_query)
# Сохраняем состояния бд
conn.commit()
# Закрываем содеинение
conn.close()
```
