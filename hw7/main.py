"""Домашка в отдельном файле рядом"""

from random import randrange
from typing import Optional

from hw7.exceptions import ValidationError
from hw7.validator import Validator, DataWithDate


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
        guess = input('Угадай число от 0 до 5: ').strip()

        try:
            guess = int(guess)
        except ValueError:
            print(f'Я поймал ошибку: Это не число')
            count_game_tries += 1
            continue

        if int(guess) != right_answer:
            print(f'Нет, попробуй ещё')
            count_game_tries += 1
            continue

        print(f'Да, ты угадал! Это действительно {guess}. Ты потратил {count_game_tries + 1} попытки(-ок)')
        break


def main():
    validator = Validator()
    history = validator.data_history
    count_validate_tries = 0

    while True:
        if len(history):
            print(f'\nЭто {count_validate_tries + 1}ая попытка ввести данные игрока')

        input_name = input('Введите Ваше имя: ')
        input_age = input('Введите Ваш возраст: ')

        new_data_with_date = DataWithDate(input_name, input_age)

        try:
            validator.validate(new_data_with_date)
        except ValidationError as e:
            print(e)
            count_validate_tries += 1
            continue
        except ValueError as e:
            print(e)
            count_validate_tries += 1
            continue

        break

    advice = get_passport_advise(int(new_data_with_date.age))
    print(f'Привет, {new_data_with_date.name.title()}! Тебе {new_data_with_date.age} лет. {advice or ""}')

    time_first_try = history[0].creation_date
    time_last_try = history[len(history) - 1].creation_date

    print(f'\nОбщее количество попыток: {len(history)}')
    print(f'Время первой попытки: {time_first_try.strftime("%H:%M:%S")}, '
          f'время последней попытки: {time_last_try.strftime("%H:%M:%S")}')
    print(f'Всего времени понадобилось: {str(time_last_try - time_first_try).split(".")[0]}')
    guess_number_game()


main()
