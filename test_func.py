import bcrypt

def hash_password(password: str) -> str:
    # Генерация соли
    salt = bcrypt.gensalt()
    # Хэширование пароля
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def check_password(password: str, hashed_password: str) -> bool:
    # Проверка пароля
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Пример использования
password = "Aa1!"
hashed_password = "$2b$12$sggdHHynqVDHp4OMPZUqDuoDU0RvHBOK/eBRVTOJh9/7NXBy9wh/S"

print(f"Исходный пароль: {password}")
print(f"Хэшированный пароль: {hashed_password}")

# Проверка пароля
is_correct = check_password(password, hashed_password)
print(f"Пароль верный: {is_correct}")
