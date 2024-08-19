"""Домашка в отдельном файле рядом"""

from random import randrange
from typing import Optional

from hw7.exceptions import ValidationError
from hw7.validator import Validator, DataWithDate
from hw9.authenticator import Authenticator
from hw9.exceptions import AuthorizationError, RegistrationError


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
    authenticator = Authenticator()

    is_user_exist = authenticator.login

    if not is_user_exist:
        print('Вы проходите регистрацию')
    else:
        print('Чтобы авторизоваться нужно ввести логин и пароль')

    while True:
        input_login = input('Введите логин: ')
        input_password = input('Введите пароль: ')

        if not is_user_exist:
            try:
                authenticator.registrate(input_login, input_password)
                print('Вы успешно зарегистрировались. Требуется авторизоваться')
                is_user_exist = True
                continue
            except RegistrationError as e:
                print(f'Ошибка: {e}')


        try:
            authenticator.authorize(input_login, input_password)
            break
        except AuthorizationError as e:
            print(f'Ошибка: {e}')


    print(f'\nВаш логин: {authenticator.login}')
    print(
        f'Время последней успешной авторизации: {authenticator.last_success_login_at.strftime("%d.%m.%Y %H:%M:%S")}')  # день.месяц.год час:минута:секунда
    print(f'{authenticator.errors_count} раз(а) пытались войти в приложение с ошибкой авторизации.')

    guess_number_game()


main()
