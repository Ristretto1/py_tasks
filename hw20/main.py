import json
from dataclasses import asdict

import requests
from bs4 import BeautifulSoup

from hw20.lesson import Lesson


def parse_lessons(url: str) -> list:
    """Функция, которая парсит сайт и выдаёт список с элементами типа Lesson преобразованными в словари"""

    # Дополнительно передаю user-agent. Иначе падает 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36'}
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    # Получаем все блоки уроков (тайтл + сабтайтлы)
    lessons_tags = soup.find_all('div', class_='t517__sectioninfowrapper')
    lessons = []

    # Проходимся по каждому, получаем тайтл и список сабтайтлов
    for lesson_tag in lessons_tags:
        title = lesson_tag.find('div', class_='t517__section-title').text

        subtitles = []
        subtitles_tags = lesson_tag.find_all('li')

        for subtitle_tag in subtitles_tags:
            subtitles.append(subtitle_tag.text)

        # Создаем экземпляр класса Lesson, переводим в словаь и аппендим в общий список с уроками
        lesson = Lesson(title, subtitles)
        lessons.append(asdict(lesson))
    return lessons


def main():
    parsed_lessons = parse_lessons('https://teachmeskills.by/kursy/obuchenie-python-online')

    with open('./lessons.json', 'w') as f:
        json.dump({
            'lessons': parsed_lessons
        }, f, ensure_ascii=False)


if __name__ == '__main__':
    main()
