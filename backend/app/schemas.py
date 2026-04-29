from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    coverImage: str

class Book(BookCreate):
    id: int