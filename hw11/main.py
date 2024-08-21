"""Домашка в отдельном файле рядом"""

from random import randrange
from hw11.authenticator import Authenticator
from hw11.exceptions import AuthorizationError, RegistrationError, ValidationError
from hw11.validator import Validator


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


def auth_loop(func):
    def wrapper():
        while True:
            result = func()
            if result:
                break

    return wrapper


authenticator = Authenticator()
validator = Validator()


@auth_loop
def main():
    is_user_exist = authenticator.email

    if not is_user_exist:
        print('Вы проходите регистрацию')
    else:
        print('Чтобы авторизоваться нужно ввести email и пароль')

    input_email = input('Введите email: ')
    input_password = input('Введите пароль: ')

    try:
        validator.validate_email(input_email)
        validator.validate_password(input_password)
    except ValidationError as e:
        print(f'Ошибка: {e}')
        return False

    if is_user_exist:
        try:
            authenticator.authorize(input_email, input_password)
        except AuthorizationError as e:
            print(f'Ошибка: {e}')
            return False

        print(f'\nВаш email: {authenticator.email}')
        print(f'Успешная авторизация в: {authenticator.last_success_login_at.strftime("%d.%m.%Y %H:%M:%S")}')
        print(f'{authenticator.errors_count} раз(а) пытались войти в приложение с ошибкой авторизации.')

        guess_number_game()
        return True

    try:
        authenticator.registrate(input_email, input_password)
        print('Вы успешно зарегистрировались. Требуется авторизоваться')
    except RegistrationError as e:
        print(f'Ошибка: {e}')
        return False


main()
