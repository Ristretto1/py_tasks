import json
import os
import bcrypt

from datetime import datetime
from typing import Optional

from hw11.exceptions import AuthorizationError, RegistrationError


class Authenticator:
    def __init__(self):
        self.email: Optional[str] = None
        self.hashed_password: Optional[str] = None
        self.last_success_login_at: Optional[datetime] = None
        self.errors_count: int = 0

        if self._is_auth_file_exist():
            self._read_auth_file()

    @staticmethod
    def _is_auth_file_exist() -> bool:
        """Метод проверяет файл, что он существует"""

        return os.path.exists('./auth.json')

    def _read_auth_file(self):
        """Метод, читающий авторизационный файл и сохраняет их"""

        with open('./auth.json') as f:
            parsed_data = json.load(f)

            self.email = parsed_data['email']
            self.hashed_password = parsed_data['hashed_password']
            self.last_success_login_at = datetime.fromisoformat(parsed_data['last_success_login_at'])
            self.errors_count = parsed_data['errors_count']

    def _update_auth_file(self):
        """Метод, перезаписывающий авторизационные данные"""

        with open('./auth.json', 'w') as f:
            json.dump({
                'email': self.email,
                'hashed_password': self.hashed_password,
                'last_success_login_at': datetime.utcnow().isoformat(),
                'errors_count': self.errors_count
            }, f)

    def registrate(self, email, password):
        """Метод, позволяющий провести регистрацию по логину и паролю"""

        if self._is_auth_file_exist():
            raise RegistrationError('auth file exist')

        if self.email is not None:
            self.errors_count += 1
            raise RegistrationError('email is not None')

        self.email = email
        self.hashed_password = self._hash_password(password)
        self.last_success_login_at = datetime.utcnow()
        self._update_auth_file()

    def authorize(self, email: str, password: str):
        """Метод, позволяющий провести авторизацию по логину и паролю"""

        if not self._is_auth_file_exist():
            raise AuthorizationError('auth file don\'t exist')

        if not self.email:
            self.errors_count += 1
            raise AuthorizationError('email is None')

        if email != self.email or not self._check_password(password, self.hashed_password):
            self.errors_count += 1
            raise AuthorizationError('Неверный логин или пароль')

        self._update_auth_file()

    @staticmethod
    def _hash_password(password: str):
        """Метод создает соль и хеширует пароль"""

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def _check_password(password: str, hashed_password: str) -> bool:
        """Метод сравнивает пароль и хеш"""

        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
