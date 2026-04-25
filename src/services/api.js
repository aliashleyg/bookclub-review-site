const API_URL = 'http://127.0.0.1:8000'

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