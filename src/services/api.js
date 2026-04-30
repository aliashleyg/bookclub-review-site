const API_URL = 'http://127.0.0.1:8000'
const apiKey = import.meta.env.VITE_GOOGLE_BOOKS_API_KEY;

export async function getBooks() {
    const res = await fetch(`${API_URL}/books`)
    return res.json()
}

export async function createBook(bookData) {
    const res = await fetch(`${API_URL}/books`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bookData),
    })
    return res.json()
}

export async function deleteBook(id) {
    const res = await fetch(`${API_URL}/books/${id}`, {
        method: 'DELETE'
    })
    return res.json()
}

export async function updateBook(id, bookData) {
    const res = await fetch(`${API_URL}/books/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bookData),
    })
    return res.json()
}

export async function searchGoogleBooks(query) {
    const res = await fetch(`https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(query)}&key=${apiKey}`)
    return res.json()
}
