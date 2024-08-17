"""Домашка:
1. Сделать последнюю домашку
2. Сделать функцию is_palindrome, которая определяет является ли строка палиндромом или нет.
При этом введено может быть как слово, так и целые предложения с пробелами и с различными знаками препинания.
Необходимо избегать всех символов кроме букв. А также не копировать входящие данные
(например, развернуть строку через срез — это скопировать входящие данные)
3. Функции на проверку имени, возраста и совет паспорт должны возвращать None
(иначе говоря, ничего не должны возвращать), если не было ошибок или нет советов
4. Сделать функцию, которая генерирует случайное число от 0 до 10,
и в бесконечном цикле просит пользователя угадать это число, если пользователь ввёл имя и возраст корректные"""
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


# print('<ПУСТАЯ СТРОКА>', is_palindrome(''))
# print('kik', is_palindrome('kik'))
# print('kir', is_palindrome('kir'))
# print('k ik', is_palindrome('k ik'))
# print('k ir', is_palindrome('k ir'))
# print('k i!k', is_palindrome('k i!k'))
# print('k i!r', is_palindrome('k i!r'))


def validate_age(age: str) -> str:
    """Проверяет, является ли возраст допустимым"""

    if not age:
        return 'Ошибка: Нужно обязательно ввести возраст'

    age = int(age)
    if age <= 0:
        return 'Ошибка: Возраст не может быть отрицательным или равен нулю'
    if age < 14:
        return 'Ошибка: Минимальный возраст — 14 лет.'


def validate_name(name: str) -> str:
    """Проверяет, является ли имя допустимым"""

    if not name:
        return 'Ошибка: Пустое имя.'
    if len(name) < 3:
        return 'Ошибка: В имени должно быть минимум 3 символа.'
    if name.count(' ') > 1:
        return 'Ошибка: Допустимое кол-во пробелов в имени - 1'


def advise_change_passport(age: int) -> Optional[str]:
    """Выдаёт совет про паспорт согласно возрастным рамкам"""

    if 16 <= age <= 17:
        return 'Нужно не забыть получить первый паспорт.'
    if 25 <= age <= 26:
        return 'Нужно не забыть заменить паспорт.'
    if 45 <= age <= 46:
        return 'Нужно не забыть второй раз заменить паспорт.'
    return None


def start_game():
    """Начинает бесконечную игру на угадывание числа от 0 до 10"""

    while True:
        right_answer = randrange(0, 11)
        guess = input('Угадай число от 0 до 10: ')

        if not guess:
            print('Нужно ввести число. Попробуй еще')
            continue

        if int(guess) == right_answer:
            print(f'Да, ты угадал! Это действительно {guess}')
        else:
            print(f'Нет, это было {right_answer}, попробуй ещё')


def main():
    input_name = input('Введите Ваше имя: ').strip()
    input_age = input('Введите Ваш возраст: ')

    error_age = validate_age(input_age)
    error_name = validate_name(input_name)

    if error_age or error_name:
        print(error_age or error_name)
        main()
    else:
        advice = advise_change_passport(int(input_age))
        print(f'Привет, {input_name.title()}! Тебе {input_age} лет. {advice or ""}')
        start_game()


main()
