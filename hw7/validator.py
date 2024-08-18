from datetime import datetime

from hw7.exceptions import ValidationError


class Data:
    """Класс, хранящий информацию об игроке"""

    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces()

    def _clear_whitespaces(self):
        """Удаляет пробелы в начале и в конце строки"""

        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    """Дочерний класс класса Date, но с записью время создания"""

    def __init__(self, name, age):
        super().__init__(name, age)
        self.creation_date = datetime.utcnow()


class Validator:
    """Класс валидирующий данные полученные от пользователя и записывает данные в историю"""

    def __init__(self):
        self.data_history: list[Data] = []

    def validate(self, data: Data):
        """Метод валидирующий данные полученные от пользователя и записывает данные в историю"""

        self.data_history.append(data)
        self._validate_name()
        self._validate_age()

    def _validate_name(self):
        """Проверяет, является ли имя допустимым"""

        try:
            last_data = self.data_history[len(self.data_history) - 1]
        except ValueError:
            raise ValueError('Ошибка: Список данных пуст')

        name = last_data.name
        if not name:
            raise ValidationError('Ошибка: Пустое имя.')
        if len(name) < 3:
            raise ValidationError('Ошибка: В имени должно быть минимум 3 символа.')
        if name.count(' ') > 1:
            raise ValidationError('Ошибка: Допустимое кол-во пробелов в имени - 1')
        return

    def _validate_age(self):
        """Проверяет, является ли возраст допустимым"""

        try:
            last_data = self.data_history[len(self.data_history) - 1]
        except ValueError:
            raise ValueError('Ошибка: Список данных пуст')

        try:
            age = int(last_data.age)
        except ValueError:
            raise ValueError(f'Ошибка: Возраст должен быть числом')

        if age <= 0:
            raise ValidationError('Ошибка: Возраст не может быть отрицательным или равен нулю')
        if age < 14:
            raise ValidationError('Ошибка: Минимальный возраст — 14 лет.')
        return
