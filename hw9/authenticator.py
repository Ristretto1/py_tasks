import os
from datetime import datetime
from typing import Optional

from hw9.exceptions import AuthorizationError, RegistrationError


class Authenticator:
    def __init__(self):
        self.login: Optional[str] = None
        self._password: Optional[str] = None
        self.last_success_login_at: Optional[datetime] = None
        self.errors_count: int = 0

        if self._is_auth_file_exist():
            self._read_auth_file()

    def _is_auth_file_exist(self) -> bool:
        """Метод проверяет файл, что он существует"""

        return os.path.exists('./auth.txt')

    def _read_auth_file(self):
        """Метод, читающий авторизационный файл и сохраняет их"""

        with open('./auth.txt') as f:
            self.login = f.readline().strip()
            self._password = f.readline().strip()
            self.last_success_login_at = datetime.fromisoformat((f.readline().strip()))
            self.errors_count = int(f.readline().strip())

    def _update_auth_file(self):
        """Метод, перезаписывающий авторизационные данные"""

        with open('./auth.txt', 'w') as f:
            f.write(f'{self.login}\n')
            f.write(f'{self._password}\n')
            f.write(f'{datetime.utcnow().isoformat()}\n')
            f.write(f'{self.errors_count}')

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
