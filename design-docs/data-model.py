# from enum import Enum, unique
from datetime import date, datetime
from typing import Dict, List, Optional, Set, TypedDict, Tuple


class TwoDPoint:
    x: int
    y: int


class BBox:
    upper_left: TwoDPoint
    bottom_right: TwoDPoint


Emotion = str


class Person(TypedDict):
    _id: str  # hash(name, birthday)
    name: str
    birthday: Optional[date]


class PersonInPicture(TypedDict, total=False):
    person_id: str
    face_position: Optional[BBox]
    body_position: Optional[List[TwoDPoint]]
        

gps = Tuple[float, float]


class Picture(TypedDict):
    _id: hash_digest
    creation_date: datetime
    coordinates: gps
    tags: dict
    Faces: List[BBox]
    people: List[PersonInPicture]

        
# indices

persons: Dict[person_id, Person]

pictures_to_files: Dict[picture_id, filepath]
