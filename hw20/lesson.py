from dataclasses import dataclass
from typing import List


@dataclass
class Lesson:
    title: str
    subtitles: List[str]
