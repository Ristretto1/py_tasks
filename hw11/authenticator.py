import json
import os
from datetime import datetime
from typing import Optional

from hw11.exceptions import AuthorizationError, RegistrationError


class Authenticator:
    def __init__(self):
        self.login: Optional[str] = None
        self._password: Optional[str] = None
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

            self.login = parsed_data.login
            self._password = parsed_data.password
            self.last_success_login_at = datetime.fromisoformat(parsed_data.last_success_login_at)
            self.errors_count = parsed_data.errors_count

    def _update_auth_file(self):
        """Метод, перезаписывающий авторизационные данные"""

        with open('./auth.json', 'w') as f:
            json.dump({
                'login': self.login,
                'password': self._password,
                'last_success_login_at': datetime.utcnow().isoformat(),
                'errors_count': self.errors_count
            }, f)

    def registrate(self, login, password):
        """Метод, позволяющий провести регистрацию по логину и паролю"""

        if self._is_auth_file_exist():
            raise RegistrationError('auth file exist')

        if self.login is not None:
            self.errors_count += 1
            raise RegistrationError('login is not None')

        self.login = login
        self._password = password
        self.last_success_login_at = datetime.utcnow()
        self._update_auth_file()

    def authorize(self, login: str, password: str):
        """Метод, позволяющий провести авторизацию по логину и паролю"""

        if not self._is_auth_file_exist():
            raise AuthorizationError('auth file don\'t exist')

        if not self.login:
            self.errors_count += 1
            raise AuthorizationError('login is None')

        if login != self.login or password != self._password:
            self.errors_count += 1
            raise AuthorizationError('Неверный логин или пароль')

        # self.errors_count = 0
        self._update_auth_file()
