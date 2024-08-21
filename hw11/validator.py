import re

from hw11.exceptions import ValidationError


# Хэшировать пароль любым алгоритмом на выбор,
# обосновать в комменте выбор алгоритма (можно хоть свой сделать).


class Validator:

    @staticmethod
    def validate_password(password: str):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};":\\|,.<>\/?]).{4,}$'
        if not re.match(pattern, password):
            raise ValidationError('Пароль не валидный')

    @staticmethod
    def validate_email(email: str):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValidationError('Email не валидный')
