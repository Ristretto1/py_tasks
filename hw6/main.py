"""Домашка в отдельном файле рядом"""
from random import randrange
from typing import Optional


def is_palindrome(value) -> bool:
    """Проверяет является ли слово палиндромом"""

    value = value.lower().strip()
    i = 0
    k = len(value) - 1

    while i <= k:
        if not value[i].isalpha():
            i += 1
            continue
        if not value[k].isalpha():
            k -= 1
            continue
        if value[i] != value[k]:
            return False

        i += 1
        k -= 1

    return True


def clear_whitespaces(value: str) -> str:
    """Удаляет пробелы в начале и в конце строки"""

    return value.strip()


def validate_age(age: int):
    """Проверяет, является ли возраст допустимым"""

    if age <= 0:
        raise Exception('Ошибка: Возраст не может быть отрицательным или равен нулю')
    if age < 14:
        raise Exception('Ошибка: Минимальный возраст — 14 лет.')
    return


def validate_name(name: str):
    """Проверяет, является ли имя допустимым"""

    if not name:
        raise Exception('Ошибка: Пустое имя.')
    if len(name) < 3:
        raise Exception('Ошибка: В имени должно быть минимум 3 символа.')
    if name.count(' ') > 1:
        raise Exception('Ошибка: Допустимое кол-во пробелов в имени - 1')
    return


def get_passport_advise(age: int) -> Optional[str]:
    """Выдаёт совет про паспорт согласно возрастным рамкам"""

    if 16 <= age <= 17:
        return 'Нужно не забыть получить первый паспорт.'
    if 25 <= age <= 26:
        return 'Нужно не забыть заменить паспорт.'
    if 45 <= age <= 46:
        return 'Нужно не забыть второй раз заменить паспорт.'
    return None


def guess_number_game():
    """Игра Угадай число от 0 до 5"""

    right_answer = randrange(0, 6)
    count_game_tries = 0

    while True:
        count_game_tries += 1
        guess = input('Угадай число от 0 до 5: ')

        if not guess.strip():
            print('Нужно ввести число. Попробуй еще')
            continue

        if int(guess) == right_answer:
            print(f'Да, ты угадал! Это действительно {guess}. Ты потратил {count_game_tries} попытки(-ок)')
            break
        else:
            print(f'Нет, попробуй ещё')


def main():
    count_validate_tries = 0

    while True:
        count_validate_tries += 1
        print()  # Это для отделения блоков попыток в консоли
        print(f'Это {count_validate_tries}ая попытка ввести данные игрока')
        input_name = clear_whitespaces(input('Введите Ваше имя: '))
        input_age = input('Введите Ваш возраст: ')

        try:
            input_age = int(input_age)
        except ValueError as e:
            print(f'Я поймал ошибку "Неправильный формат возраста": {e}')
            continue

        try:
            validate_age(input_age)
            validate_name(input_name)
            break
        except Exception as e:
            print(f'Я поймал ошибку: {e}')

    advice = get_passport_advise(input_age)
    print(f'Привет, {input_name.title()}! Тебе {input_age} лет. {advice or ""}')
    guess_number_game()


main()
