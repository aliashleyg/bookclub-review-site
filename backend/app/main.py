from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import BookCreate, Book

app = FastAPI()

# allow your Vue app to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # fine for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/books")
def get_books():
    return [
        {
            "id": 1,
            "title": "THIS CAME FROM FASTAPI",
            "author": "Backend Test",
            "genre": "Test Genre",
            "description": "If you see this, the frontend is loading data from the API.",
            "coverImage": "https://via.placeholder.com/200x300"
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

@app.post("/books")
def create_book(book: BookCreate):
    new_book = Book(
        id=3,
        title=book.title,
        author=book.author,
        genre=book.genre,
        description=book.description,
        coverImage=book.coverImage
    )
    return new_book