from __future__ import annotations
from dataclasses import dataclass, asdict

from fixturedemo.db import DB

@dataclass
class Book:
    id: int | None = None
    author: str | None = None
    title: str | None = None
    genre: str | None = None
    read: bool = False

    @classmethod
    def from_dict(cls, d: dict) -> Book:
        return cls(**d)
    
    def to_dict(self) -> dict:
        return asdict(self)


class NotFoundException(ValueError):
    pass


class BookDao:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path, "books")

    def insert(self, book: Book) -> int:
        id = self._db.create(book.to_dict())
        self._db.update(id, {"id": id})
        return id
    
    def get(self, id: int) -> Book:
        record = self._db.read(id)
        if record is None:
            raise NotFoundException(f"no book found with the provided id: {id}")

        return Book.from_dict(record)
    
    def delete(self, id: int) -> None:
        try:
            self._db.delete(id)
        except KeyError as exc:
            raise NotFoundException(f"no book to delete with the provided id: {id}") from exc

    def delete_all(self) -> None:
        self._db.delete_all()

    def count(self) -> int:
        return self._db.count()

    def close(self) -> None:
        self._db.close()
