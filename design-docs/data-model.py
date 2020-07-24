# from enum import Enum, unique
from datetime import date, datetime
from typing import List, TypedDict


class BBox:
    x1: int
    y1: int
    x2: int
    y2: int


Emotion = str

class Face(TypedDict):
    manual: bool  # is it manually added/reviewed? 
    emotion: Emotion
    position: BBox


class Person(TypedDict):
    _id: str  # hash(name, birthday)
    name: str
    birthday: date


persons: Dict[person_id, Person]


class PersonInPicture(TypedDict):
    person_id: str
    position: List[Points]


gps = Tuple[float, float]


class CustomAttributes:  # tags?
    pass

class Picture(TypedDict):
    _id: hash_digest
    creation_date: datetime
    coordinates: gps
    tags: Set[str]
    Faces: List[BBox]
    people: List[person_id]


pictures_to_files: Dict[picture_id, filepath]
