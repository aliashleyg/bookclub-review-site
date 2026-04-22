from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import BookCreate
app = FastAPI()

# allow your Vue app to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # fine for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

books = [
    {
        "id": 1,
        "title": "THIS CAME FROM FASTAPI",
        "author": "Backend Test",
        "genre": "Test Genre",
        "description": "If you see this, the frontend is loading data from the API.",
        "coverImage": "https://upload.wikimedia.org/wikipedia/commons/c/c8/HMCoFirstEdSecondPrintTitle.jpg"
    },
    {
        "id": 2,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "genre": "History",
        "description": "A history novel by Leo Tolstoy",
        "coverImage": "https://upload.wikimedia.org/wikipedia/commons/c/c8/HMCoFirstEdSecondPrintTitle.jpg"
    }
]

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def create_book(book: BookCreate):
    if not books:
        next_id = 1
    else:
        ids = []
        for current_book in books:
            ids.append(current_book["id"])
        next_id = max(ids) + 1
    new_book = {
        "id": next_id,
        "title": book.title,
        "author": book.author,
        "coverImage": book.coverImage,
        "genre": book.genre,
        "description": book.description
        }
    books.append(new_book)
    return new_book

@app.delete("/books/{id}")
def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": f"Book deleted successfully"}
    return {"message": f"Book with id {id} not found"}

