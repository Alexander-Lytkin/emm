### Лекция 14. Unit-тестирование

* При решении задач всегда нужно проверять их на адекватность.
* До этого, вы сдавали задачи и проверяли по сценарию:
    * Написали полотно
    * Запустили -> бросили что-то на вход 
    * Получили что-то на выходе -> сравнили с желаемым результатом

* Такой подход будем называть ***полным тестированием***

### Шаг 0. Полное тестирвоание - это плохо
* Плохо это, потому что:
    * Если возникнет ошибка в коде - не понятно, где именно
    * Если ошибки будут переркрываться (самое ужасное) то будет создаваться впечателение, что написан просто ***убер-код***, а на самом деле он вообще не работоспособен.
    * !!! Нет гарантии, что после изменений вашего кода, он сохранит работоспособность !!!

### Шаг 1. Unit-тестирование - это хорошо
* Требует одного простого действия - необходимо декомпозировать код
* ***Декомпозиция*** - процесс разделения одной большой задачи на несколько маленьких (независимых друг от друга) подзадач.
* В результате декомпозиции код разделяется на набор функций/классов.
* Основное правило декомпозиции - ***любой программный юнит делает одно действие, и делает его хорошо***

### Шаг 2. Декомпозированный код
* Рассмотрим пример ```code.py```
```
"""
module with erros
"""

def add(a_arg:int, b_arg:int):
    """
    return sum of a_arg and b_arg
    """
    return a_arg + b_arg - 2

def sub(a_arg:int, b_arg:int):
    """
    return a_arg - b_arg
    """
    return a_arg - b_arg + a_arg // b_arg

def mult(a_arg:int, b_arg:int):
    """
    return a_arg * b_arg
    """
    return a_arg + b_arg

def main():
    """
    Start
    """
    result = add(2,3) + sub(3,4) + mult(1,5)
    print(result)

if __name__ == "__main__":
    main()
```

* В этом коде основной интерес представляют юниты ```add, sub, mult```. ```main``` не особо интересен, т.к. в нем используются предедыщие 3 юнита + ```print()```. 

* Создадим модуль ```code_test.py``` (в python принято создавать тестовые модули по правило ```<module_name>_test.py```)
* Определим там тестовый класс
```
"""
Тестовый модуль для code.py
"""
import unittest

class TestCode(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
```

* Тестовый класс необходимо называть со слова ```Test```.
* Тестовый класс необходио наследовать от ```unittest.Test...```
* Не забываем вызвать ```unittest.main()``` - подцепит все классы ,которые были унаследованы через ```unitttest```.

* Теперь определим сами тесты. Тесты определяются в виде методов тестового класса. Каждый метод должен начинаться со слова ```test_```
```
"""
Тестовый модуль для code.py
"""
import unittest
import code

class TestCode(unittest.TestCase):
    def test_add(self):
        pass

    def test_sub(self):
        pass

    def test_mult(self):
        pass



if __name__ == "__main__":
    unittest.main()
```

* Напишем первый тест!
```
"""
Тестовый модуль для code.py
"""
import unittest
import code

class TestCode(unittest.TestCase):
    def test_add(self):
        """
        Тест юнита add()
        """
        self.assertEqual(code.add(1,1), 2) # Тестовый случай
        self.assertEqual(code.add(0, 0), 0)
        self.assertEqual(code.add(-10, 10), 0)
        self.assertEqual(code.add(4, 5), 9)
        self.assertEqual(code.add(-2, -7), -9)

    def test_sub(self):
        """
        Тест юнита sub()
        """
        self.assertEqual(code.sub(1,1), 0) # Тестовый случай
        self.assertEqual(code.sub(10, 2), 8)
        self.assertEqual(code.sub(-10, 10), -20)
        self.assertEqual(code.sub(10, -3), 13)
        self.assertEqual(code.sub(-24, 0), -24)

    def test_mult(self):
        """
        Тест юнита mult()
        """
        self.assertEqual(code.mult(2,2), 4)
        self.assertEqual(code.mult(0,2), 0)
        self.assertEqual(code.mult(10,10), 100)
        self.assertEqual(code.mult(-2,-2), 4)
        self.assertEqual(code.mult(3,-4), -12)



if __name__ == "__main__":
    unittest.main()
```

* Запустим!
```
python  -m unittest -v code_test.py
```

### Шаг 3. На будущее
* Достаточно популярный сторонний фреймворк для модульных тестов ```pytest```.


### Шаг 4. Самостоятельная работа по алгоритмическим задачам
* ***Ссылка*** : https://contest.yandex.ru/contest/27951/problems/
* Длительность 1.5 часа
* Нужно сделать как можно больше!
* На обед 50 мин
* Начнем лекцию ~ 15:30