# from enum import Enum, unique
from datetime import date, datetime
from typing import List, Optional, TypedDict


class Point:
    x: int
    y: int

        
class BBox:
    upper_left: Point
    bottom_right: Point


class Person(TypedDict):
    _id: str  # hash(name, birthday)
    name: str
    birthday: Optional[date]


class PersonInPicture(TypedDict, total=False):
    person_id: str
    face_position: Optional[BBox]
    body_position: Optional[List[Points]]
        

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
